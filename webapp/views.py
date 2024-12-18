from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactUsForm

def home(request):
    return render(request, 'home.html')

def contact_us_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        requirement = request.POST.get('requirement')

        # Save the form data to the database
        contact_us_entry = ContactUsForm(
            name=name,
            email=email,
            phone_number=phone_number,
            requirement=requirement
        )
        contact_us_entry.save()

        # Return a success response
        return JsonResponse({'success': True})

    return render(request, "contact_us_form.html")
