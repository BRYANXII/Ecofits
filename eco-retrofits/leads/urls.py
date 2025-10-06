# leads/urls.py
from django.urls import path
from .views import lead_capture, thank_you

urlpatterns = [
    path('', lead_capture, name='lead_capture'),
    path('thank-you/', thank_you, name='thank_you'),
]