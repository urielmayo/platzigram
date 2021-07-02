from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from users.models import Profile

# Create your views here.
def login_view(request):
    
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
    logout(request)
    return redirect('login')

def signup_view(request):
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
