#django modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.urls import reverse, reverse_lazy

#django models
from django.contrib.auth.models import User

#forms
from users.forms import ProfileForm, SignUpForm

#project models
from posts.models import Post

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

            return redirect(
                reverse('users:detail',
                kwargs ={'username':request.user.username}
                )
            )
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

    
    
