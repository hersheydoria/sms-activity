from django import forms

class SMSForm(forms.Form):
    phone_number = forms.CharField(label="Phone Number", max_length=15)
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        allowed_numbers = ['+639700919275', '+639074833701']
        if phone_number not in allowed_numbers:
            raise forms.ValidationError(
                f"Only the following numbers are allowed: {', '.join(allowed_numbers)}."
            )
        return phone_number
