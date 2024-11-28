import vonage
from django.conf import settings

def send_sms(to_number, message):
    client = vonage.Client(
        key=settings.VONAGE_API_KEY,
        secret=settings.VONAGE_API_SECRET
    )
    sms = vonage.Sms(client)

    response = sms.send_message(
        {
            "from": "VonageAPI",
            "to": to_number,
            "text": message,
        }
    )

    # Ensure a consistent return format
    if response["messages"][0]["status"] == "0":
        return {
            "status": "0",
            "message": "Message sent successfully."
        }
    else:
        return {
            "status": response["messages"][0]["status"],
            "error": response["messages"][0].get("error-text", "Unknown error.")
        }
