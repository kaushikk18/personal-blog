from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    all_posts = Post.objects.all()
    return render(request, 'index.html', {'posts': all_posts})


def post(request, title):
    posts = Post.objects.get(title=title)
    return render(request, 'posts.html', {'posts': posts})
