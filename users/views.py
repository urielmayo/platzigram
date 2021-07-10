#django modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy

#django models
from django.contrib.auth.models import User

#forms
from users.forms import ProfileForm, SignUpForm

#project models
from posts.models import Post
from users.models import Profile

# Create your views here.
def login_view(request):
    """login view"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        
        if user:
            login(request, user)
            return redirect('posts:feed')
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
    return redirect('users:login')

class UpdateProfileView(LoginRequiredMixin, UpdateView):

    template_name = 'users/update_profile.html'
    model = Profile
    fields = [
        'website',
        'biography',
        'phone_number',
        'profile_picture',
    ]

    def get_object(self):
        """returns User's profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        
        username = self.object.user.username
        return reverse(
            'users:detail',
            kwargs= {
                'username':username
            }
        )


class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignUpView(FormView):

    template_name = 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Saves the new user"""
        form.save()
        return super().form_valid(form)

    
    
