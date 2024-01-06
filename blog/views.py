from django.shortcuts import render
from .models import Post
# Create your views here.


def blog(requests):
    posts = Post.objects.all()
    return render(requests, 'blog/blog.html', {'posts': posts})
