from django.shortcuts import render
from networkspace.forms import ContactForm
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("09e80z@gmail.com", "wrqc itej rnar jcad")



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form data here (e.g., save to database or send email)
            print(form.cleaned_data)
            data_acqs = dict(form.cleaned_data)
            data_acq=""
            for i,j in data_acqs.items():
                data_acq += "\n"+str(i)+"\n"+str(j)
            message = data_acq
            s.sendmail("09e80z@gmail.com", "networkspace.in@gmail.com", message)
            s.quit()
            return render(request, 'networkspace/success.html')  # Create this page
    else:
        form = ContactForm()
    return render(request, 'networkspace/contact.html', {'form': form})

