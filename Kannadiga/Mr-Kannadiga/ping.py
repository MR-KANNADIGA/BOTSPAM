import os
YOUR_NAME = os.environ.get("YOUR_NAME, None")
from .. import *
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@bot.on(events.NewMessage(pattern="/ping"))
@bot2.on(events.NewMessage(pattern="/ping"))
@bot3.on(events.NewMessage(pattern="/ping"))
@bot4.on(events.NewMessage(pattern="/ping"))
@bot5.on(events.NewMessage(pattern="/ping"))
@bot6.on(events.NewMessage(pattern="/ping"))
@bot7.on(events.NewMessage(pattern="/ping"))
@bot8.on(events.NewMessage(pattern="/ping"))
@bot9.on(events.NewMessage(pattern="/ping"))
@bot10.on(events.NewMessage(pattern="/ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "ಹೇಳು ಮಚಾ!💕"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"💛 ಹೇಳು ಮಾಮ್ ಯಾವ್ ಸುಳೆ ಬೋಳಿ ಮಗಂದ್ ಮುಕ್ಲಿ ಹಾಡ್ಬೇಕ್ ❤️\n`{ms}` 𝗺𝘀\n  My Master :- {YOUR_NAME}")                       
