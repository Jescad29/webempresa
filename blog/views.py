from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.


def blog(requests):
    posts = Post.objects.all()
    return render(requests, 'blog/blog.html', {'posts': posts})


def category(requests, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(requests, 'blog/category.html', {'category': category, 'posts': posts})
