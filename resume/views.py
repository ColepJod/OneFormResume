# resume/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resume
from .forms import ResumeForm

def home_view(request):
    """
    Home page view - shows website info and login/register buttons.
    """
    return render(request, 'home.html')


@login_required
def dashboard_view(request):
    """
    Dashboard view - shows options after login.
    
    @login_required means: only logged-in users can access this page.
    If not logged in, user is redirected to login page.
    """
    
    # Check if user already has a resume
    try:
        resume = Resume.objects.get(user=request.user)
        has_resume = True
    except Resume.DoesNotExist:
        resume = None
        has_resume = False
    
    context = {
        'has_resume': has_resume,
        'resume': resume,
    }
    
    return render(request, 'resume/dashboard.html', context)


@login_required
def resume_create_view(request):
    """
    View to create a new resume.
    Only accessible if user doesn't have a resume yet.
    """
    
    # Check if user already has a resume
    try:
        existing_resume = Resume.objects.get(user=request.user)
        # User already has resume, redirect to edit page
        messages.info(request, 'You already have a resume. You can edit it below.')
        return redirect('resume_edit')
    except Resume.DoesNotExist:
        pass  # No resume exists, continue to create one
    
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        
        if form.is_valid():
            # Create resume but don't save to database yet
            resume = form.save(commit=False)
            
            # Set the user to current logged-in user
            resume.user = request.user
            
            # Now save to database
            resume.save()
            
            messages.success(request, 'Your resume has been created successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request - show empty form
        form = ResumeForm()
    
    context = {
        'form': form,
        'title': 'Create Your Resume',
        'button_text': 'Create Resume',
    }
    
    return render(request, 'resume/resume_form.html', context)


@login_required
def resume_edit_view(request):
    """
    View to edit an existing resume.
    Only accessible if user already has a resume.
    """
    
    # Try to get user's existing resume
    try:
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        # No resume exists, redirect to create page
        messages.info(request, 'You need to create a resume first.')
        return redirect('resume_create')
    
    if request.method == 'POST':
        # Pass instance=resume to update existing resume (not create new one)
        form = ResumeForm(request.POST, instance=resume)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Your resume has been updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request - show form filled with existing data
        form = ResumeForm(instance=resume)
    
    context = {
        'form': form,
        'title': 'Edit Your Resume',
        'button_text': 'Save Changes',
    }
    
    return render(request, 'resume/resume_form.html', context)


@login_required
def portfolio_view(request):
    """
    View to display user's portfolio/resume page.
    """
    
    # Try to get user's resume
    try:
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        messages.warning(request, 'Please create your resume first.')
        return redirect('resume_create')
    
    # Split skills into a list for better display
    skills_list = []
    if resume.skills:
        # Split by comma and clean up whitespace
        skills_list = [skill.strip() for skill in resume.skills.split(',') if skill.strip()]
    
    context = {
        'resume': resume,
        'skills_list': skills_list,
    }
    
    return render(request, 'resume/portfolio.html', context)