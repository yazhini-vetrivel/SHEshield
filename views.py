from django.conf import settings
from twilio.rest import Client
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import EmergencyContact, UnsafeAreaReport
from rest_framework import serializers

# Serializer for Heatmap (Step 4)
class HeatmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnsafeAreaReport
        fields = ['latitude', 'longitude', 'risk_level']

# --- STEP 3: SOS TRIGGER ---
class TriggerSOS(APIView):
    permission_classes = [IsAuthenticated] # Ensures user is logged in

    def post(self, request):
        user = request.user
        location_url = request.data.get('location_url', 'Location not provided')
        
        # Fetch contacts
        contacts = EmergencyContact.objects.filter(user=user)
        
        if not contacts.exists():
            return Response({"error": "No emergency contacts found"}, status=status.HTTP_400_BAD_REQUEST)

        # Initialize Twilio
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            
            for contact in contacts:
                client.messages.create(
                    body=f"🚨 ALERT: {user.username} triggered an SOS! View location: {location_url}",
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=contact.phone_number
                )
            return Response({"status": "Alerts sent successfully!"}, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- STEP 4: HEATMAP API ---
class HeatmapDataView(generics.ListAPIView):
    queryset = UnsafeAreaReport.objects.all()
    serializer_class = HeatmapSerializer
