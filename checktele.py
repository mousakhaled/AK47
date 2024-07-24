import random
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UsernameOccupied, UsernameInvalid, FloodWait, RPCError
from queue import Queue
import requests
from user_agent import generate_user_agent
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'
zz = 'qwertyuiopassdfghjklzxcvbnm'
zzz = 'qwertyuiopassdfghjklzxcvbmn' #:(

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()

def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1": #aaabc
        c = random.choices(a)
        d = random.choices(zz)
        s = random.choices(zzz)
        f = [c[0], c[0], c[0], d[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(zz)
            s = random.choices(zzz)
            f = [c[0], d[0], d[0], d[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2": #abbbc
        c = random.choices(a)
        d = random.choices(zz)
        s = random.choices(zzz)
        f = [c[0], d[0], d[0], d[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(zz)
            s = random.choices(zzz)
            f = [c[0], d[0], s[0], s[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "3": #abccc
        c = random.choices(a)
        d = random.choices(zz)
        s = random.choices(zzz)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(zz)
            s = random.choices(zzz)
            f = [c[0], c[0], c[0], d[0], s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "4": #a1ccc
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(zzz)
        f = [c[0], d[0], s[0], s[0], s[0]]
        username = ''.join(f)
    if choice == "5": #aaa1c
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(zzz)
        f = [c[0], c[0], c[0], d[0], s[0]]
        username = ''.join(f)
    if choice == "6": #aaab1
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(zzz)
        f = [c[0], c[0], c[0], s[0], d[0]]
        username = ''.join(f)
    if choice == "7": #abbb1
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(zzz)
        f = [c[0], s[0], s[0], s[0], d[0]]
        username = ''.join(f)
    if choice == "8":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username + 'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username + 'bot'
        else:
            pass
    return username

app = Client("my_account")

@app.on_message(filters.command("تشيكر تلي") & filters.me)
async def tele_checker(client, message):
    if ispay2[0] == "yes":
        await message.edit(tele_checker)
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.command("اليوزرات المبندة") & filters.me)
async def send_banned(client, message):
    if ispay2[0] == "yes":
        await client.send_document(message.chat.id, 'banned.txt')
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.command("الانواع") & filters.me)
async def show_types(client, message):
    if ispay2[0] == "yes":
        await message.edit(tele_checker2)
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.regex(r"^\.كلايم (\d+) (\d+) (.*)") & filters.me)
async def claimer(client, message):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = message.text.split()
        attempts = int(msg[1])
        choice = msg[2]
        ch = msg[3]
        trys = 0
        await message.edit(f"حسناً سأفحص نوع {choice} من اليوزرات على {ch} , بعدد {attempts} من المحاولات !")

        async def claimer_status(client, message):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await message.edit(f"الكلايم وصل لـ({trys}) من المحاولات")
                elif "off" in isclaim:
                    await message.edit("لايوجد كلايم شغال !")  
                else:
                    await message.edit("حدث خطأ غير معروف")
            else:
                await message.edit("يجب الدفع لاستعمال هذا الامر !")

        async def claimer_details(client, message):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await message.reply(f"Attempts: ({trys}) \nType: {choice}")
                elif "off" in isclaim:
                    await message.reply("Claimer is not working ⚠️ !")
                else:
                    await message.edit("حدث خطأ غير معروف")
            else:
                await message.edit("يجب الدفع لاستعمال هذا الامر !")

        app.add_handler(MessageHandler(claimer_status, filters.command("حالة الكلايم") & filters.me))
        app.add_handler(MessageHandler(claimer_details, filters.command("الكلايم") & filters.me))

        while isclaim[0] == "on":
            username = gen_user(choice)
            if check_user(username) == "Available":
                try:
                    await client.set_chat_username(ch, username)
                    await client.send_message(message.chat.id, f"User claimed @{username}")
                    await client.send_message(message.chat.id, f"Attempts: {trys} ")
                    isclaim.clear()
                    isclaim.append("off")
                except UsernameOccupied:
                    await client.send_message(message.chat.id, f"اليوزر مأخوذ بالفعل: @{username}")
                except UsernameInvalid:
                    pass
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except RPCError as e:
                    await client.send_message(message.chat.id, f
                    await client.send_message(message.chat.id, f"حدث خطأ: {e}")
            trys += 1
            await asyncio.sleep(1)
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.command("كلايم توقيف") & filters.me)
async def stop_claimer(client, message):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("off")
        await message.edit("تم توقيف الكلايم !")
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.regex(r"^\.اوتو (\d+) (\d+) (.*)") & filters.me)
async def auto(client, message):
    if ispay2[0] == "yes":
        isauto.clear()
        isauto.append("on")
        msg = message.text.split()
        choice = msg[2]
        ch = msg[3]
        trys = 0
        await message.edit(f"حسناً سأبدأ العمل على {choice} من اليوزرات على {ch} !")

        while isauto[0] == "on":
            username = gen_user(choice)
            if check_user(username) == "Available":
                try:
                    await client.set_chat_username(ch, username)
                    await client.send_message(message.chat.id, f"User catched @{username} 🐊\nAttempts: {trys}")
                except UsernameOccupied:
                    pass
                except UsernameInvalid:
                    pass
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except RPCError as e:
                    await client.send_message(message.chat.id, f"حدث خطأ: {e}")
            trys += 1
            await asyncio.sleep(1)
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

@app.on_message(filters.command("اوتو توقيف") & filters.me)
async def stop_auto(client, message):
    if ispay2[0] == "yes":
        isauto.clear()
        isauto.append("off")
        await message.edit("تم توقيف الاوتو !")
    else:
        await message.edit("يجب الدفع لاستعمال هذا الامر !")

app.run()
