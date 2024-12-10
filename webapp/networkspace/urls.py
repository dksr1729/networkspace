from django.urls import path
from networkspace.views import contact_view

urlpatterns = [
    path('', contact_view, name='contact'),
]
