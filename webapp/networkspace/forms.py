from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Name', 'class': 'form-input'
    }))
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'placeholder': 'Enter Your Mobile Number', 'class': 'form-input'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your Email Address', 'class': 'form-input'
    }))
    requirement = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your Requirement', 'class': 'form-textarea'
    }))
