from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from posts.models import Post
from django.shortcuts import redirect

from users.models import Profile
#post detail view
class PostDetailView(LoginRequiredMixin, DetailView):
    
    template_name= 'posts/detail.html'
    model = Post
    context_object_name = 'post'

#feed view
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    context_object_name = 'posts'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_followers = context['view'].request.user.profile.follows.all()
        context['posts'] = Post.objects.filter(profile__in= profile_followers).order_by('-created')
        return context
    

#new post
class CreatePostView(LoginRequiredMixin, CreateView):

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

@login_required
def liked_photo(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    liked_users = post.liked.all()
    print(liked_users)
    profile = request.user.profile

    if profile not in liked_users:
        post.liked.add(profile)
    else:
        post.liked.remove(profile)
    return redirect('posts:feed')