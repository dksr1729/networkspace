from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/submit-contact/', views.submit_contact_form, name='submit_contact_form'),
]
