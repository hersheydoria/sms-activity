Django SMS Application

This is a simple Django web application that allows users to send SMS messages using the Vonage SMS API. The application includes input validation, the ability to send predefined templates, and scheduling for periodic SMS sending. The templates allow users to select common message types (e.g., "Survey Reminder", "Order Shipped") to streamline the message creation process.

Features:
- Send SMS messages to predefined registered phone numbers.
- Select predefined templates for SMS content.
- User-friendly interface with a card design for easy interaction.
- Validation to allow messages only to specific phone numbers.
- Displays success or error messages for user feedback.
- Includes a "Try Again" functionality for invalid input.
- Scheduled SMS sending using Celery.
- Background task handling to send SMS messages at specified intervals (e.g., every minute).
  
Prerequisites:
- Python 3.8 or later
- Django 4.2 or later
- Vonage Python SDK (vonage)
- A Vonage account and API key/secret
- Celery for background task handling
- Redis for Celery message brokering
- Celery worker and beat services running

How It Works:

Home Page:
- Accessible at http://127.0.0.1:8000/.
- Displays a welcome message with a link to the SMS sending page.
  
Send SMS Page:
- Accessible at http://127.0.0.1:8000/sms/send-sms/.
- Users can enter:
- A phone number (must be one of the registered numbers).
- A message to send, or select from predefined templates.
- An optional scheduled time for sending the SMS.

Predefined Templates:
- Users can select from predefined templates when composing the SMS message. These templates can include common messages such as "Survey Reminder", "Order Shipped", etc.
- The templates are displayed in a dropdown list and are prefilled in the message field.
  
Validation:
- There are only specific numbers allowed.
- Invalid numbers display an error message and provide a "Try Again" link.
  
Success:
- If the message is successfully sent, the user sees a confirmation and can choose to send another SMS.

Scheduled SMS:
- The system uses Celery to handle periodic tasks (e.g., sending scheduled SMS).
- Celery worker and beat are running to send messages at regular intervals (every minute).

Usage:
- Open the home page at http://127.0.0.1:8000/ and click the "Send SMS" button.
- Select a predefined template or enter a custom message.
- Enter one of the registered numbers (e.g., +639700919275).
- Check the checkbox for a scheduled message (optional).
- Submit the form.
- View success or error messages as applicable.

How to Execute / Run
- Find the redis folder (path) and open cmd.
- Execute or run the "redis-server.exe" (don't close the cmd).
- Open Visual Studio Code terminal and execute the celery worker "celery -A sms_project worker --loglevel=info -P solo".
- In another terminal, execute the celery beat "celery -A sms_project beat --loglevel=info".
- Lastly, in another terminal, run the server using this command "python manage.py runserver".
