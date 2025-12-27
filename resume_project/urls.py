# resume_project/urls.py

from django.contrib import admin
from django.urls import path, include
from resume.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home page
    path('', home_view, name='home'),
    
    # Include accounts app URLs
    path('accounts/', include('accounts.urls')),
    
    # Include resume app URLs (we'll create this next)
    path('', include('resume.urls')),
]