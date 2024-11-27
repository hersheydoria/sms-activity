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
        print(f"Processing SMS: Phone Number: {sms.phone_number}, Message: {sms.message}")
        
        result = send_sms(sms.phone_number, sms.message)
        
        # Print the result to check its structure
        print(f"send_sms result: {result}")
        
        if result["status"] == "0":
            sms.is_sent = True
            sms.save()
        else:
            print(f"Failed to send SMS to {sms.phone_number}. Result: {result}")
