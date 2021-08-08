from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Subscription(models.Model):
    blog = models.ManyToManyField(Blog)

    def get_blogs(self):
        return ''.join([str(blogs.id) for blogs in self.blog.all()])

    def __str__(self):
        return self.get_blogs()

#
# class News(models.Model):
#     subscriptions = models.ForeignKey(Subscription, on_delete=models.CASCADE)
#
#     def get_subscriptions(self):
#         return '\n'.join([str(subscription) for subscription in self.subscriptions.all()])
#
#     def __str__(self):
#         return self.get_subscriptions
