import vonage
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import EmergencyContact, UnsafeArea
from .serializers import UnsafeAreaSerializer


class TriggerSOS(APIView):
    """
    Handles the SOS panic button. Sends SMS to all emergency contacts.
    """

    def post(self, request):
        location_url = request.data.get("location_url", "No location provided")

        # 1️⃣ Get all contacts from the database
        contacts = EmergencyContact.objects.all()

        if not contacts.exists():
            return Response(
                {"error": "No emergency contacts found in database."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 2️⃣ Validate settings
        if not all([settings.VONAGE_API_KEY, settings.VONAGE_API_SECRET, settings.VONAGE_FROM_NUMBER]):
            return Response(
                {"error": "Vonage API credentials or sender number not configured."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # 3️⃣ Initialize Vonage Client
        client = vonage.Client(
            key=settings.VONAGE_API_KEY,
            secret=settings.VONAGE_API_SECRET
        )
        sms = vonage.Sms(client)

        success_count = 0
        failed_contacts = []

        # 4️⃣ Send SMS to each contact
        for contact in contacts:
            response = sms.send_message({
                "from": settings.VONAGE_FROM_NUMBER,
                "to": contact.phone_number,
                "text": f"🚨 EMERGENCY! A user needs help. Location: {location_url}",
            })

            print(f"Vonage Response for {contact.phone_number}:", response)

            message_status = response["messages"][0]["status"]
            if message_status == "0":
                success_count += 1
            else:
                error_text = response["messages"][0].get("error-text")
                failed_contacts.append({"phone": contact.phone_number, "error": error_text})
                print(f"Failed to send to {contact.phone_number} — Error: {error_text}")

        result = {
            "status": "Completed",
            "success_count": success_count,
            "failed": failed_contacts
        }

        return Response(result, status=status.HTTP_200_OK)


class HeatmapData(APIView):
    """
    Returns a list of unsafe coordinates for the map display.
    """

    def get(self, request):
        areas = UnsafeArea.objects.all()
        serializer = UnsafeAreaSerializer(areas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
