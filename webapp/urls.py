from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact_us_form/', views.contact_us_form, name='contact_us_form'),
    path('contact_us/', views.contact_us_form, name='contact_us'),
]
