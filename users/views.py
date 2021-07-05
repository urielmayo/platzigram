#django modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

#models
from users.models import Profile

#forms
from users.forms import ProfileForm

# Create your views here.
def login_view(request):
    """login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return redirect('feed')
        else:
            error_context = {
                'error': 'Invalid username or password. Try Again Please',
                'retry_username': username
            }
            return render(request, 'users/login.html',context = error_context)
        
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect('login')

def signup_view(request):
    """signup view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_conf = request.POST['password_conf']

        #validates password
        if password != password_conf:
            return render(request, 'users/signup.html',{'error':'Password confirmation differs from password'})
        #verifies new username is unique
        elif User.objects.filter(username=username):
            return render(request, 'users/signup.html',{'error':'User already exists'})
        
        #register user
        user = User.objects.create_user(
            username=username,
            password=password, 
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email']
        )

        profile = Profile(
            user=user
        )
        profile.save()
        return redirect('login')


    return render(request, 'users/signup.html')

@login_required
def update_profile(request):
    """update profile data view"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.profile_picture = data['profile_picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request,
        'users/update_profile.html',
        context={
        'profile':profile,
        'user': request.user,
        'form': form,
        },
    )