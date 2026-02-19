import vonage

client = vonage.Client(key="def57267", secret="48arl1PM*kK")
sms = vonage.Sms(client)

response = sms.send_message({
    "from": "VonageAPI",
    "to": "+916383345337",
    "text": "Test message"
})
print(response)
