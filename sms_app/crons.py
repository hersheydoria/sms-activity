from django.conf import settings
import vonage
from django_cron import CronJobBase, Schedule

class SendSMSCronJob(CronJobBase):
    RUN_EVERY_MINS = 5  # Schedule this job to run every 5 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'sms_app.send_sms_cron'  # Unique identifier for this cron job

    def do(self):
        # Access the Vonage API credentials from Django settings
        client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
        sms = vonage.Sms(client)

        response = sms.send_message(
            {
                "from": "YourAppName",
                "to": "RECIPIENT_PHONE_NUMBER",  # Replace with a real recipient phone number
                "text": "This is a scheduled SMS from Django!",
            }
        )

        if response["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {response['messages'][0]['error-text']}")
