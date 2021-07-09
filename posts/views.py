from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from datetime import datetime
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm
from posts.models import Post



#feed view
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

#new view
@login_required
def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    context = {
        'form':form,
        'user':request.user,
        'profile':request.user.profile,
    }

    return render(request, 'posts/new.html',context=context)