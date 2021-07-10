from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy

from posts.forms import PostForm
from posts.models import Post

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
    ordering = ('-created',)
    paginate_by = 5
    context_object_name = 'posts'

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