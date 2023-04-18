import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# class skill(models.Model):
#     name = models.CharField(max_length=500)

#     def __str__(self):
#         return self.name

# class Genre(models.Model):
#     country = models.ForeignKey(skill_role, on_delete=models.CASCADE)
#     name = models.CharField(max_length=500)

#     def __str__(self):
#         return self.name

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    # skill_role = models.ForeignKey(skill, on_delete=models.SET_NULL, null=True)
    # genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    # user roles
    # add widget on front end that allows users to select multiple skills
    # skills = (
    #     ('Fashion Designer', 'Fashion Designer'),
    #     ('VisualArtist', 'VisualArtist'),
    #     ('Clothing reseller', 'Clothing reseller'),
    #     ('Musician', 'Musician'),
    #     ('Videographer', 'Videographer'),
    #     ('Photographer', 'Photographer'),
    #     ('Dancer', 'Dancer'),
    #     ('Sculpter', 'Sculpter'),
    # )
    skill_role = models.CharField(max_length=100, blank=True)
    # make a second skill role
    # make a third skill role

    # models.CharField(
    #     max_length=17,
    #     choices=skills,
    #     default='VisualArtist',
    # )

    # fd_genre = [
    #     ('Streetwear', 'Streetwear'),
    #     ('Punk', 'Punk'),
    #     ('Minimalism', 'Minimalism'),
    #     ('Vintage', 'Vintage'),
    #     ('Gothic', 'Gothic'),
    #     ('Hippie', 'Hippie'),
    #     ('Country', 'Country'),
    # ]

    # fd_genre_role = models.CharField(
    #     max_length=10,
    #     choices=fd_genre,
    #     default='StreetWear',
    # )
    # art_genre = [
    #     ('NFT', 'NFT'),
    #     ('Abstract', 'Abstract'),
    #     ('Realism', 'Realism'),
    #     ('Surrealism', 'Surrealism'),
    #     ('Futurism', 'Futurism'),
    #     ('Modernism', 'Modernism'),
    #     ('Minimalism', 'Minimalism'),
    #     ('Post Moderism', 'Post Moderism'),
    #     ('Symbolism', 'Symbolism'),
    #     ('Politcalism', 'Politcalism'),
    #     ('Classicism', 'Classicism'),
    #     ('Opiticalism', 'Opiticalism'),
    # ]

    # art_genre_role = models.CharField(
    #     max_length=13,
    #     choices=art_genre,
    #     default='Abstract',
    # )
    # music_genre = [
    #     ('HipHop', 'HipHop'),
    #     ('Rock', 'Rock'),
    #     ('Rap', 'Rap'),
    #     ('Blues', 'Blues'),
    #     ('Country', 'Country'),
    #     ('Indie', 'Indie'),
    #     ('Pop', 'Pop'),
    #     ('Drill', 'Drill'),
    #     ('Punk', 'Punk'),
    #     ('Funk', 'Funk'),
    #     ('Lofi', 'Lofi'),
    #     ('Techno', 'Techno'),
    #     ('R&B', 'R&B'),
    #     ('Soul', 'Soul'),
    #     ('Folk', 'Folk'),
    # ]

    # music_genre_role = models.CharField(
    #     max_length=7,
    #     choices=music_genre,
    #     default='HipHop',
    # )
    # reseller_genre = [
    #     ('Designer', 'Designer'),
    #     ('Sneakers', 'Sneakers'),
    #     ('StreetWear', 'StreetWear'),
    #     ('Vintage', 'Vintage'),
    #     ('Custom', 'Custom'),
    # ]
    # reseller_genre_role = models.CharField(
    #     max_length=10,
    #     choices=reseller_genre,
    #     default='StreetWear',
    # )

    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    post_id = models.CharField(max_length=500)
    comment = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class VidComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    post_id = models.CharField(max_length=500)
    comment = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class BlogComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    post_id = models.CharField(max_length=500)
    comment = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class MusicComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    post_id = models.CharField(max_length=500)
    comment = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(Comment, blank=True)

    # add specific features tailroed to each type of post

    def __str__(self):
        return self.user


class vidpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vidposts_files')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # add comment feature

    def __str__(self):
        return self.user


class musicpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='musicpost_files')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # add comment feature

    def __str__(self):
        return self.user


class blogpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # add comment feature

    def __str__(self):
        return self.user


class storepost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # add comment feature

    def __str__(self):
        return self.user


class forumpost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='forum_post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    # add comment feature

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
