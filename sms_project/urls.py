from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sms/', include('sms_app.urls')),  # Include SMS app URLs
    path('', home_view, name='home'),       # Add a route for the root URL
]
