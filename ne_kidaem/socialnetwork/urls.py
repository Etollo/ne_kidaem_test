from django.urls import path

from .views import blog_list, news_list

urlpatterns = [
    path('', blog_list, name='blog_list_url'),
    path('news/', news_list, name='news_list_url')
]