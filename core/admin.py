from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount, vidpost, blogpost, storepost, musicpost, forumpost, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(vidpost)
admin.site.register(blogpost)
admin.site.register(storepost)
admin.site.register(musicpost)
admin.site.register(forumpost)
admin.site.register(LikePost)
admin.site.register(Comment)
admin.site.register(FollowersCount)
