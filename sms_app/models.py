from django.db import models
from django.utils.timezone import now

class ScheduledSMS(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"To: {self.phone_number} at {self.scheduled_time} (Sent: {self.is_sent})"
    
class SMSTemplate(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
