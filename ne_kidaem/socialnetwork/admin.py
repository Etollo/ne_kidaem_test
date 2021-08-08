from .models import *


@admin.register(Blog, Post, Subscription, News)
class Admin(admin.ModelAdmin):
    pass



