**Django SMS Application**

This is a simple Django web application that allows users to send SMS messages using the Vonage SMS API. The application includes input validation to ensure that only specific registered phone numbers can be used.

Features:
- Send SMS messages to predefined registered phone numbers.
- User-friendly interface with a card design.
- Validation to allow messages only to specific phone numbers.
- Displays success or error messages for user feedback.
- "Try Again" functionality for invalid input.

Prerequisites:
- Python 3.8 or later
- Django 4.2 or later
- Vonage Python SDK (vonage)
- A Vonage account and API key/secret

**How It Works**

Home Page:
- Accessible at http://127.0.0.1:8000/.
- Displays a welcome message with a link to the SMS sending page.
  
Send SMS Page:
- Accessible at http://127.0.0.1:8000/sms/send-sms/.
- Users can enter:
- A phone number (must be one of the registered numbers).
- A message to send.
  
Validation:
- There are only specific numbers allowed.
- Invalid numbers display an error message and provide a "Try Again" link.
  
Success:
- If the message is successfully sent, the user sees a confirmation and can choose to send another SMS.

Usage:
- Open the home page at http://127.0.0.1:8000/ and click the "Send SMS" button.
- Enter one of the registered numbers (+639700919275 or +639074833701) and your message.
- Submit the form.
- View success or error messages as applicable.
