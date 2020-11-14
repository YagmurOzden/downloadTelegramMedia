import configparser
import json

from telethon import TelegramClient, functions, types
import asyncio
from asyncio import run
import datetime
import time
# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

phone = config['Telegram']['phone']
username = config['Telegram']['username']

############################# ************************************* #############################
client = TelegramClient(username, api_id, api_hash)

async def downloadTelegramMedia():

    # You can print the message history of any chat:
    async with TelegramClient(username, api_id, api_hash) as client:
        #Ensure you're authorized
        if not client.is_user_authorized():
            await client.send_code_request(phone)
            try:
                await client.sign_in(phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))
        

        async for message in client.iter_messages('group link'):
            if message.media is not None:
                
                A=str(message.media)
                A=A.replace(" ","").replace("\n","").split("datetime")
                date_time_str = A[2]
        
                date_time_str=date_time_str.replace("(","").replace(",tzinfo=","").split(",")
                
                #date_time_obj = str(datetime.datetime.strptime(date_time_str, '%Y,%m,%d,%H'))
                x = datetime.datetime(int(date_time_str[0]),int(date_time_str[1]),int(date_time_str[2]))
                x=str(x.strftime('%Y-%m-%d'))
                
    
                #bugünün tarihi
                today = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                today=today.split("-")
                x=x.split("-")
                today=["2020","11","13"]
                if today[0]==x[0] and today[1]==x[1] and today[2]==x[2] :
                    await message.download_media("path the media folder")

                
                

asyncio.run(downloadTelegramMedia())
