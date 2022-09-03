import configparser
import json
import asyncio
import sqlite3

from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import events
from telethon import connection
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import CheckChatInviteRequest

from datetime import date, datetime

#function to check, if
def inMessage(str_, words):
    for word in words:
        if word.lower() in str_.lower():
            return True
    return False

config = configparser.ConfigParser()
config.read("config.ini")

#getting needable information from config
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
my_channel = config['Telegram']['my_channel']

#reading urls from file
UrlsFile = open("channels.txt", "r")
urls = UrlsFile.read().splitlines()
UrlsFile.close

urls = [int(url) for url in urls]

#reading keywords from file
KeysFile = open("keywords.txt", "r")
keywords = KeysFile.read().splitlines()
KeysFile.close

#creating tg client
client = TelegramClient(username, api_id, api_hash)

#to get updates
@client.on(events.NewMessage(chats=urls))
async def handler_new_message(event):
    try:
        #if no validation is needable, just delete this "if"
        if inMessage(event.raw_text, keywords):
            await client.forward_messages(my_channel, event.message)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
