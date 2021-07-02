from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
    return render(request, 'users/signup.html')
