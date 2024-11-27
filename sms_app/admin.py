from django.contrib import admin
from .models import SMSTemplate

@admin.register(SMSTemplate)
class SMSTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'content')  # Display the 'name' and 'content' fields in the admin list
