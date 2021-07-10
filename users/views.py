#django modules
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

#django models
from django.contrib.auth.models import User

#forms
from users.forms import SignUpForm

#project models
from posts.models import Post
from users.models import Profile

# Create your views here.
class LoginView(auth_views.LoginView):
    """Login View Class"""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View Class"""

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

    
    
