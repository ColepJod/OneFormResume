# resume/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Dashboard - shown after login
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Resume CRUD operations
    path('resume/create/', views.resume_create_view, name='resume_create'),
    path('resume/edit/', views.resume_edit_view, name='resume_edit'),
    
    # Portfolio view
    path('portfolio/', views.portfolio_view, name='portfolio'),
    
    # PDF Download (placeholder - we'll implement in Part 5)
    path('resume/download/', views.portfolio_view, name='download_pdf'),  # Temporary!
]