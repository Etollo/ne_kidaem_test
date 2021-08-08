from django.shortcuts import render

from .models import Post, Subscription


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'socialnetwork/index.html', context={'posts': posts})


def news_list(request):
    post = [temp.blog.id for temp in Post.objects.all()]
    print(post)

    subscriptions = [subscriptions for subscriptions in Subscription.objects.all()]
    print(subscriptions)

    blog_id = 0
    for i, j in subscriptions, post:
        if i == j:
            blog_id = j

    print(blog_id)
    news = [post.title for post in Post.objects.all()]
    return render(request, 'socialnetwork/news_list.html', context={'news': news})
