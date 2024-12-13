from django.shortcuts import render
from .models import ContactUs
from django.http import JsonResponse

def home(request):
    return render(request, 'webapp/home.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        requirement = request.POST.get('requirement')

        # Save to database
        ContactUs.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            requirement=requirement,
        )
        return JsonResponse({'success': True, 'message': 'Successfully submitted!'})

    return render(request, 'webapp/contactus.html')