django-admin startproject gas_utilities_project
cd gas_utilities_project
python manage.py startapp consumer_services
# consumer_services/models.py

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for account information (e.g., billing details)
# consumer_services/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

@login_required
def submit_request(request):
    if request.method == 'POST':
        # Process form submission
        # Create a new service request object
        # Save request details
        return redirect('request_tracking')
    return render(request, 'submit_request.html')

@login_required
def track_request(request):
    # Retrieve service requests for the current user
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_request.html', {'service_requests': service_requests})

@login_required
def view_account(request):
    # Retrieve account information for the current user
    # Render account details template
    return render(request, 'account_details.html')
# gas_utilities_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('consumer/', include('consumer_services.urls')),
]
# consumer_services/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('submit_request/', views.submit_request, name='submit_request'),
    path('track_request/', views.track_request, name='track_request'),
    path('view_account/', views.view_account, name='view_account'),
]
