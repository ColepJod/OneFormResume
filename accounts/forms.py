# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    """
    Custom registration form that extends Django's built-in UserCreationForm.
    We add an email field because the default form doesn't include it.
    """
    
    # Add email field (required)
    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address."
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        """
        Customize the form appearance by adding CSS classes.
        """
        super().__init__(*args, **kwargs)
        
        # Add CSS class to all fields for styling
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-input'
            })
        
        # Add placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
    
    def save(self, commit=True):
        """
        Save the user and include the email.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user