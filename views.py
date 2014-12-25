from django.shortcuts import render
from blog.models import Post, Tag


def front(request):
    posts = Post.objects.all()
    return render(request, 'front.html', {'posts': posts})


def post(request, slug):
    post = Post.objects.slug(slug)
    return render(request, 'post.html', {'post': post})


def user(request, username):
    posts = Post.objects.user(username)
    return render(request, 'front.html', {'posts': posts})


def year(request, year):
    posts = Post.objects.year(year)
    return render(request, 'front.html', {'posts': posts})


def month(request, year, month):
    posts = Post.objects.month(year, month)
    return render(request, 'front.html', {'posts': posts})


def tag(request, slug):
    posts = Post.objects.tag(slug)
    return render(request, 'front.html', {'posts': posts})


def category(request, slug):
    posts = Post.objects.category(slug)
    return render(request, 'front.html', {'posts': posts})
