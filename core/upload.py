from instabot import Bot
import random
import string
from django.core.files.storage import default_storage
import os  

#change file path when uploaded to server
#fix upload file size

class InstaPost():
    def instapost(theimage, thecaption, filetype='.jpg'):

        bot = Bot()
        bot.login(username='hajbibiii',
                password='=[WEfH9>EM9(^mW',
                is_threaded=True)
                
        path = os.getcwd()+'media/temp/'

        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=15))

        filename=str(res)+filetype

        with open(os.path.join(path, filename), 'w') as fp:
            pass

        with default_storage.open('temp/'+filename, 'wb+') as destination:
            for chunk in theimage.chunks():
                destination.write(chunk)

        bot.upload_photo(path+filename, caption=thecaption)

        os.remove(path+filename+".REMOVE_ME")

        return True

# class YtPost():
#     #https://github.com/redianmarku/youtube-autoupload-bot/blob/master/main.py

# class tiktokPost():
#     #https://github.com/redianmarku/tiktok-autouploader/blob/main/run.py
#     #https://www.ayrshare.com/tiktok-api-how-to-post-to-tiktok-using-a-social-media-api/

# class RedditPost():

# class SoundCloudPost():

# class SpotifyPost():

# class TwitterPost():

# class ShopifyPost():


