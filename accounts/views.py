# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    """
    Handle user registration.
    
    GET request: Show empty registration form
    POST request: Process form data and create user
    """
    
    # If user is already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        # User submitted the form
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            # Form data is valid, save the user
            user = form.save()
            
            # Log the user in automatically after registration
            login(request, user)
            
            # Show success message
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            
            # Redirect to dashboard
            return redirect('dashboard')
        else:
            # Form has errors, show error message
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request: show empty form
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Handle user login.
    
    GET request: Show login form
    POST request: Authenticate and log user in
    """
    
    # If user is already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        # User submitted the form
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            # Get username and password from form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user (check if username/password are correct)
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # User exists and password is correct
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        # GET request: show empty form
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Handle user logout.
    """
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')