from django.contrib import admin
from django.urls import path
from leads.views import lead_capture, thank_you

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lead_capture, name='lead_capture'),
    path('thank-you/', thank_you, name='thank_you'),
]