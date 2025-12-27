# resume/models.py

from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    """
    This model stores all resume data for a user.
    Each user can have only ONE resume (OneToOneField).
    """
    
    # Link this resume to a user account
    # OneToOneField means: 1 user = 1 resume (not multiple resumes)
    # on_delete=models.CASCADE means: if user is deleted, delete their resume too
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Personal Information
    full_name = models.CharField(max_length=100)
    
    # TextField is for longer text (no character limit)
    about_me = models.TextField(blank=True)
    
    # Skills, Education, Projects, Experience - all can be long text
    skills = models.TextField(blank=True, help_text="Enter your skills separated by commas")
    education = models.TextField(blank=True)
    projects = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    
    # Contact Information
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    contact_address = models.TextField(blank=True)
    
    # Social Links
    linkedin = models.URLField(blank=True, help_text="Your LinkedIn profile URL")
    github = models.URLField(blank=True, help_text="Your GitHub profile URL")
    
    # Timestamps - automatically track when resume was created/updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # This method defines what to show when we print a Resume object
    def __str__(self):
        return f"{self.full_name}'s Resume"
    
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"