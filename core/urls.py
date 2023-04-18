from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('uploadvideo', views.uploadvideo, name='uploadvideo'),
    path('uploadblog', views.uploadblog, name='uploadblog'),
    path('uploadmusic', views.uploadmusic, name='uploadmusic'),
    path('uploadstore', views.uploadstore, name='uploadforum'),
    path('uploadforum', views.upload, name='uploadforum'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('comment-post', views.comment_post, name='comment-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('etsy', views.etsyLogin, name='etsyLogin'),
    path('ebay', views.ebaylogin, name='ebay')
    # path('chat/<str:room_name>', views.chat, name="chat")
]
