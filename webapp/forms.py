from django import forms
from .models import ContactUsForm

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsForm
        fields = ['name', 'email', 'phone_number', 'requirement']
