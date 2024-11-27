from django.shortcuts import render
from .forms import SMSForm
from .models import ScheduledSMS
from .utils import send_sms
from django.utils.timezone import now

def send_sms_view(request):
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            scheduled_time = form.cleaned_data.get('scheduled_time')
            schedule_sms = form.cleaned_data.get('schedule_sms')
            template = form.cleaned_data.get('template')

            # Use template content if no custom message is entered
            if not message and template:
                message = template.content

            # If no message and no template selected, show an error
            if not message:
                result = "Please enter a message or select a template."
                return render(request, 'sms_app/send_sms.html', {
                    "form": form,
                    "result": result,
                })

            if schedule_sms and scheduled_time:
                # Save as scheduled SMS
                ScheduledSMS.objects.create(
                    phone_number=phone_number,
                    message=message,
                    scheduled_time=scheduled_time,
                )
                result = f"Message scheduled successfully for {scheduled_time}!"
            else:
                # Send SMS immediately
                result_data = send_sms(phone_number, message)

                # Handle response from send_sms
                if isinstance(result_data, dict) and "status" in result_data:
                    if result_data["status"] == "0":
                        result = f"Message sent successfully to {phone_number}!"
                    else:
                        result = f"Error: {result_data['error-text']}"
                else:
                    result = f"Unexpected response: {result_data}"

            return render(request, 'sms_app/send_sms.html', {
                "form": form,
                "result": result,
            })
    else:
        form = SMSForm()

    return render(request, 'sms_app/send_sms.html', {"form": form})
