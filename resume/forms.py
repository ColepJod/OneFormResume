# resume/forms.py

from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    """
    Form for creating and editing resume data.
    ModelForm automatically creates form fields from the model.
    """
    
    class Meta:
        model = Resume
        
        # Don't include 'user' - we'll set that automatically
        # Don't include timestamps - they're automatic
        fields = [
            'full_name',
            'about_me',
            'skills',
            'education',
            'projects',
            'experience',
            'contact_email',
            'contact_phone',
            'contact_address',
            'linkedin',
            'github',
        ]
        
        # Customize the form widgets (how fields look)
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name'
            }),
            'about_me': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Write a brief introduction about yourself...',
                'rows': 4
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Example: Python, Django, HTML, CSS, JavaScript',
                'rows': 3
            }),
            'education': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Example:\nB.Tech in Computer Science\nXYZ University (2018-2022)\nGPA: 8.5/10',
                'rows': 4
            }),
            'projects': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Example:\n1. Resume Builder Website\n   - Built with Django\n   - Features: PDF generation, user auth',
                'rows': 5
            }),
            'experience': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Example:\nSoftware Developer at ABC Company\nJan 2022 - Present\n- Developed web applications\n- Worked with Python and Django',
                'rows': 5
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'your.email@example.com'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+1 234 567 8900'
            }),
            'contact_address': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'City, State, Country',
                'rows': 2
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://linkedin.com/in/yourprofile'
            }),
            'github': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'https://github.com/yourusername'
            }),
        }
        
        # Custom labels for fields
        labels = {
            'full_name': 'Full Name',
            'about_me': 'About Me',
            'skills': 'Skills',
            'education': 'Education',
            'projects': 'Projects',
            'experience': 'Work Experience',
            'contact_email': 'Email Address',
            'contact_phone': 'Phone Number',
            'contact_address': 'Address',
            'linkedin': 'LinkedIn Profile',
            'github': 'GitHub Profile',
        }
        
        # Help text for fields
        help_texts = {
            'skills': 'List your skills separated by commas',
            'education': 'Include degree, institution, year, and grades',
            'projects': 'Describe your key projects with technologies used',
            'experience': 'List your work experience with responsibilities',
        }