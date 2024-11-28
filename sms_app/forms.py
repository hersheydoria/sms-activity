from django import forms
from django.utils.timezone import now
from .models import SMSTemplate

class SMSForm(forms.Form):
    template = forms.ModelChoiceField(queryset=SMSTemplate.objects.all(), required=False, label="Template")
    phone_number = forms.CharField(label="Phone Number", max_length=15)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=False)
    scheduled_time = forms.DateTimeField(
        label="Schedule Time (optional)",
        required=False,
        initial=now,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    schedule_sms = forms.BooleanField(
        required=False,
        label="Schedule this message?",
        initial=False,
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        allowed_numbers = ['+639918815563']
        if phone_number not in allowed_numbers:
            raise forms.ValidationError(
                f"Only the following numbers are allowed: {', '.join(allowed_numbers)}."
            )
        return phone_number

    def clean_message(self):
        message = self.cleaned_data.get('message')
        template = self.cleaned_data.get('template')

        # If message is empty, populate it with the selected template content
        if not message and template:
            return template.content

        # If no message and no template selected, raise an error
        if not message:
            raise forms.ValidationError("Please enter a message or select a template.")
        
        return message

    def clean_scheduled_time(self):
        scheduled_time = self.cleaned_data.get('scheduled_time')
        schedule_sms = self.cleaned_data.get('schedule_sms')

        # Only validate scheduled time if the checkbox is checked
        if schedule_sms and scheduled_time:
            if scheduled_time < now():
                raise forms.ValidationError("Scheduled time must be in the future.")
        
        return scheduled_time
