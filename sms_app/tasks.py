from celery import shared_task
from .models import ScheduledSMS
from .utils import send_sms
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_scheduled_sms():
    unsent_sms = ScheduledSMS.objects.filter(is_sent=False, scheduled_time__lte=now())
    for sms in unsent_sms:
        try:
            print(f"Processing SMS: Phone Number: {sms.phone_number}, Message: {sms.message}")
            result = send_sms(sms.phone_number, sms.message)
            
            if result["status"] == "0":
                sms.is_sent = True
                sms.save()
                print(result["message"])
            else:
                print(f"Failed to send SMS to {sms.phone_number}. Error: {result.get('error')}")
        except Exception as e:
            print(f"Error processing SMS for {sms.phone_number}: {e}")
