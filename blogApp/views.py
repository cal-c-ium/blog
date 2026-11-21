from django.shortcuts import render
from blogApp.models import Post

# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blogApp/index.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blogApp/detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blogApp/category.html", context)