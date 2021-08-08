from django.shortcuts import render

from .models import Post


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'socialnetwork/index.html', context={'posts': posts})
