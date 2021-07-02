from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    error_context = {
        'error': 'Invalid username or password. Try Again Please'
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html',context = error_context)
        
    return render(request, 'users/login.html')