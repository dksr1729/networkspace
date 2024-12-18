from django.contrib import admin
from .models import ContactUsForm

@admin.register(ContactUsForm)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'requirement')
