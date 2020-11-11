import configparser
import json

from telethon import TelegramClient, functions, types
import asyncio
from asyncio import run

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

############################# ************************************* #############################
client = TelegramClient(username, api_id, api_hash)
client.start()
print("Client Created")


async def downloadTelegramMedia():

    # You can print the message history of any chat:
    async with TelegramClient('session', api_id, api_hash) as client:
        #Ensure you're authorized
        if not client.is_user_authorized():
            await client.send_code_request(phone)
            try:
                await client.sign_in(phone, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))
        

        async for message in client.iter_messages('https://t.me/'):
            if message.media is not None:
                await message.download_media("/home/yamur/Desktop/telegram/")
                print(message.sender.username, message.media)

asyncio.run(downloadTelegramMedia())
