import json

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import RegisterForm, ContactForm
from .models import Contact, UserProfile
from .fitness_ai import process_message


def index_view(request):
    """Home page view"""
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    return render(request, 'index.html', {'form': form})


def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('profile')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'login.html')


@login_required
def profile_view(request):
    """User profile view"""
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None
    
    context = {
        'user': user,
        'profile': profile,
    }
    
    return render(request, 'profile.html', context)


@require_POST
def ai_coach_view(request):
    """Fitness AI coach API endpoint."""
    try:
        data = json.loads(request.body)
        message = data.get('message', '').strip()
        context = data.get('context', {})
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'error': 'Invalid request'}, status=400)

    if not message:
        return JsonResponse({'error': 'Message required'}, status=400)

    result = process_message(message, context)
    return JsonResponse(result)

