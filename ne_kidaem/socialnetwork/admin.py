from .models import *


@admin.register(Blog, Post, Subscription)
class Admin(admin.ModelAdmin):
    pass



