import random
from itertools import chain

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from instagram.client import InstagramAPI

from .models import Profile, Post, LikePost, FollowersCount, blogpost, vidpost, musicpost, forumpost, storepost, Comment
from .upload import InstaPost

client_id = '1312196812972649'
client_secret = 'c18e25473b8ac7a63e4daf0ce749d153'


# Create your views here.
@login_required(login_url='signup')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    user_following_list = []
    feed = []
    comments = []
    vidfeed = []
    musicfeed = []
    storefeed = []
    blogfeed = []
    forumfeed = []
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if (x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    return render(request, 'index.html', {'user_profile': user_profile, 'posts': feed_list,
                                          'suggestions_username_profile_list': suggestions_username_profile_list[:4]})


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # fix file size error when uploading
        # add settings to allow user to login to their instagram previously.
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        InstaPost.instapost(image, caption)
        return redirect('/')
    return render(request, 'upload.html')


@login_required(login_url='signin')
def uploadvideo(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # make method that allow users to select what type of post
        new_post = vidpost.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'uploadvideo.html')


@login_required(login_url='signin')
def uploadblog(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # make method that allow users to select what type of post
        new_post = blogpost.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'uploadblog.html')


@login_required(login_url='signin')
def uploadmusic(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # make method that allow users to select what type of post
        new_post = musicpost.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'uploadmusic.html')


@login_required(login_url='signin')
def uploadstore(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # make method that allsow users to select what type of post
        new_post = storepost.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'uploadstore.html')


@login_required(login_url='signin')
def uploadforum(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        # make method that allsow users to select what type of post
        new_post = forumpost.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    return render(request, 'uploadforum.html')


@login_required(login_url='signin')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        username = request.POST['username']
        username_object = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)

        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html',
                  {'user_profile': user_profile, 'username_profile_list': username_profile_list})


@login_required(login_url='signin')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def like_vidpost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = vidpost.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def like_forumpost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = forumpost.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def like_blogpost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = blogpost.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def like_musicpost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = musicpost.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def comment_post(request):
    if request.method == 'POST':
        username = request.user.username
        post_id = request.GET.get('post_id')
        post = Post.objects.get(id=post_id)
        comment = request.POST['comment']
        comment_post = Comment.objects.create(post_id=post_id, user=username, comment=comment)
        comment_post.save()
        post.comments.add(comment_post)
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def comment_vidpost(request):
    if request.method == 'POST':
        username = request.user.username
        post_id = request.GET.get('post_id')
        post = vidpost.objects.get(id=post_id)
        comment = request.POST['comment']
        comment_post = Comment.objects.create(post_id=post_id, user=username, comment=comment)
        comment_post.save()
        post.comments.add(comment_post)
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def comment_blogpost(request):
    if request.method == 'POST':
        username = request.user.username
        post_id = request.GET.get('post_id')
        post = blogpost.objects.get(id=post_id)
        comment = request.POST['comment']
        comment_post = Comment.objects.create(post_id=post_id, user=username, comment=comment)
        comment_post.save()
        post.comments.add(comment_post)
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def comment_musicpost(request):
    if request.method == 'POST':
        username = request.user.username
        post_id = request.GET.get('post_id')
        post = musicpost.objects.get(id=post_id)
        comment = request.POST['comment']
        comment_post = Comment.objects.create(post_id=post_id, user=username, comment=comment)
        comment_post.save()
        post.comments.add(comment_post)
        post.save()
        return redirect('/')


@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)
    user_blog_posts = blogpost.objects.filter(user=pk)
    user_blog_posts_length = len(user_blog_posts)
    user_forum_posts = forumpost.objects.filter(user=pk)
    user_forum_posts_length = len(user_forum_posts)
    user_music_posts = musicpost.objects.filter(user=pk)
    user_music_posts_length = len(user_music_posts)
    user_store_posts = storepost.objects.filter(user=pk)
    user_store_posts_length = len(user_store_posts)
    user_vid_posts = vidpost.objects.filter(user=pk)
    user_vid_posts_length = len(user_vid_posts)
    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        # add other options of
        'user_blog_posts': user_blog_posts,
        'user_blog_posts_length': user_blog_posts_length,
        'user_forum_posts': user_forum_posts,
        'user_forum_posts_length': user_forum_posts_length,
        'user_music_posts': user_music_posts,
        'user_music_posts_length': user_music_posts_length,
        'user_store_posts': user_store_posts,
        'user_store_posts_length': user_store_posts_length,
        'user_vid_posts': user_vid_posts,
        'user_vid_posts_length': user_vid_posts_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/' + user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/' + user)
    else:
        return redirect('/')


# @login_required(login_url='signin')
# class CreateMyModelView(CreateView):
#     model = Profile
#     form_class = skillform
#     template_name = 'myapp/settings.html'
#     success_url = 'myapp/index.html'

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    # link instagram account signin

    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']
            skill = request.POST['skill']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.skill_role = skill
            # make a second skill role
            # make a third skill role
            user_profile.save()

        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']
            skill = request.POST['skill']
            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.skill_role = skill
            user_profile.save()

        return redirect('settings')
    return render(request, 'setting.html', {'user_profile': user_profile})
    # test redirect to index


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()

                    # log user in and redirect to settings page
                    user_login = auth.authenticate(username=username, password=password)
                    auth.login(request, user_login)
                    # create a Profile object for the new user
                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return redirect('/')  # redirect to settings later
                except ValueError:
                    messages.info(request, 'Credentials Invalid')
                    return redirect('signup')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                auth.login(request, user)
                return redirect('/')
            except ValueError:
                messages.info(request, 'Credentials Invalid')
                return redirect('signin')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


import base64

path = 'https://api.sandbox.ebay.com/'
app_json = 'application/json'

clientID = 'kaveripa-unight-PRD-d5206ac65-b205be68'
clientSecret = 'PRD-3ac6ead8c3ef-dcf1-4bbd-a421-af17'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': base64.b64encode(
        b'Basic kaveripa-unight-PRD-d5206ac65-b205be68:PRD-3ac6ead8925b-e9d5-44b4-a134-5c9f'),
    # 'Authorization': 'Basic kaveripa-unight-PRD-d5206ac65-b205be68:PRD-3ac6ead8925b-e9d5-44b4-a134-5c9f',
    'Accept': 'application/json',
    'cache-control': 'no-cache'
}

body = {
    'grant_type': 'authorization_code',
    'code': 'v^1.1#i^1#f^0#p^3#r^0#I^3#t^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',
    'redirect_uri': 'http://127.0.0.1:8000/'
}


def get_oath_token():
    url = 'https://api.ebay.com/identity/v1/oauth2/token'
    r = requests.post(url, headers=headers, data=body)
    print(headers)
    print(body)
    print(r.json())


def get_oath_token_of_etsy():
    url = 'https://www.etsy.com/oauth/connect'
    response_type = 'code'

    r = requests.post(url, headers=headers, data=body)


@login_required(login_url='signin')
def ebaylogin(request):
    # ebay = OAuth1Session('kaveripa-unight-PRD-d5206ac65-b205be68',
    #                      client_secret='PRD-5206ac657f9b-0875-47d1-88f8-5c82',
    #                      resource_owner_key='resource_owner_key',
    #                      resource_owner_secret='resource_owner_secret')
    # url = 'https://api.twitter.com/1/account/settings.json'
    # r = ebay.get(url)
    headers = {
        "Authorization": "Basic  v^1.1#i^1#I^3#p^3#f^0#r^0#t^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",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    EndPoint = "https://api.ebay.com/identity/v1/oauth2/token"

    response = requests.post(EndPoint, headers=headers)

    return HttpResponse(response, 'something wrong')


@login_required(login_url='signin')
def etsyLogin(request):
    if request.method == 'GET':
        r = requests.get('https://www.etsy.com/oauth/connect', params=request.GET)

    if request.method == 'POST':
        r = requests.post('https://www.etsy.com/oauth/connect', params=request.GET)
        # cutid = 'kaveripa-unight-PRD-d5206ac65-b205be68'
        # context = {
        #     'cutid': cutid
        # }
        print(r)
        if r.status_code == 200:
            print(r)
            # return HttpResponse(r)
            return render(request, 'index.html', {'response_type': '200', 'client_id': 'd59lamjsuh31eqpg7gxc990r',
                                                  'redirect_uri': 'http://127.0.0.1:8000/',
                                                  'scope': 'profile_r%profile_w'})
        return HttpResponse('Could not save data')


def instagram(request):
    api = InstagramAPI(client_id=client_id, client_secret=client_secret)
    redirect_uri = 'http://127.0.0.1:8000/instagram/callback'
    api.access_token = api.exchange_code_for_access_token(code=request.GET['code'], redirect_uri=redirect_uri)
    media = api.user_recent_media(user_id='your_instagram_user_id', count=10)
    print(media)
    return render(request, 'index.html', {'media': media})
