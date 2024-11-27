from django.shortcuts import render
from .forms import SMSForm
from .utils import send_sms

def send_sms_view(request):
    result = None
    form = SMSForm()

    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            result = send_sms(phone_number, message)
            # Reset form to allow sending another SMS
            form = SMSForm()

    return render(request, "sms_app/send_sms.html", {"form": form, "result": result})
