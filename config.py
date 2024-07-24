from pyrogram import Client
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
SESSION = os.environ.get("TERMUX")
TOKEN = os.environ.get("TOKEN")
sedthon = Client("my_account", api_id=APP_ID, api_hash=APP_HASH, session_string=SESSION)
bot = Client("bot", api_id=APP_ID, api_hash=APP_HASH, bot_token=TOKEN)
ispay = ['yes']
ispay2 = ['yes']
sedthon.start()
bot.start()
