import json

from telethon import TelegramClient, functions, types
import os
import asyncio
import datetime
import time


from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


import TelegramKeys
import keys
# # # # # TELEGRAM AUTHENTICATE # # # # #
class TelegramAuthenticator():
    
    def __init__(self,api_id,api_hash,phone,username):

        self.api_id = TelegramKeys.api_id
        self.api_hash = TelegramKeys.api_hash

        self.phone = TelegramKeys.phone
        self.username = TelegramKeys.username


# # # # # EXTRACT PICTURE  # # # # #

class Telegram:

    async def downloadTelegramMedia(self):
        # You can print the message history of any chat:
        async with TelegramClient(telegramAuth.username, telegramAuth.api_id, telegramAuth.api_hash) as client:
            #Ensure you're authorized
            # if not client.is_user_authorized():
            #     await client.send_code_request(phone)
            #     try:
            #         await client.sign_in(phone, input('Enter the code: '))
            #     except SessionPasswordNeededError:
            #         await client.sign_in(password=input('Password: '))
            

            async for message in client.iter_messages('https://t.me/turkuazgrafik'):
                if message.media is not None:
                    
                    A=str(message.media)
                    A=A.replace(" ","").replace("\n","").split("datetime")
                    date_time_str = A[2]
            
                    date_time_str=date_time_str.replace("(","").replace(",tzinfo=","").split(",")
                    
                    #date_time_obj = str(datetime.datetime.strptime(date_time_str, '%Y,%m,%d,%H'))
                    x = datetime.datetime(int(date_time_str[0]),int(date_time_str[1]),int(date_time_str[2]))
                    x=str(x.strftime('%Y-%m-%d'))
                    
        
                    #todays date
                    today = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                    today=today.split("-")
                    x=x.split("-")

                    if today[0]==x[0] and today[1]==x[1] and today[2]==x[2] :

                        await message.download_media("media")









# # # # # TWITTER AUTHENTICATE # # # # #
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth=OAuthHandler(keys.CONSUMER_KEY,keys.CONSUMER_SECRET)
        auth.set_access_token(keys.ACCESS_TOKEN,keys.ACCESS_TOKEN_SECRET)
        return auth



class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client=API(self.auth)
        self.twitter_user=twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client


# # # # # SEND TWEET  # # # # #
class PostTweet():
    def FileOperations():
        os.chdir("media")
        dosyalar = os.listdir()
        Liste=[]
        for dosya in dosyalar:
            if dosya.endswith(".jpg"):
                Liste.append(dosya)
        return Liste[0]

    def postTweet(self):
        # Upload images and get media_ids
        filenames = [PostTweet.FileOperations()]
        media_ids = []
        for filename in filenames:
            res = twitter_api.media_upload(filename)
            media_ids.append(res.media_id)
        # Tweet with multiple images
        twitter_api.update_status(status='Vaka sayısı:', media_ids=media_ids)


if __name__=="__main__":


    #for Telegram Authenticator it gives the telegram keys
    telegramAuth=TelegramAuthenticator(TelegramKeys.api_id,TelegramKeys.api_hash,TelegramKeys.phone,TelegramKeys.username)

    mediadownloader=Telegram()

    #loop = asyncio.get_event_loop()


    #asyncio.run(mediadownloader.downloadTelegramMedia())
    #task = asyncio(mediadownloader.downloadTelegramMedia())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(mediadownloader.downloadTelegramMedia())
    loop.close()

    #for Twitter Authenticator it gives the telegram keys
    twitter_client=TwitterClient()
    twitter_api=twitter_client.get_twitter_client_api()

    #for tweeting
    tweet=PostTweet()
    tweet.postTweet()
    


