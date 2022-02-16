import os
YOUR_NAME = os.environ.get("YOUR_NAME, None")
from .. import *
from telethon import events
from time import time
from datetime import datetime

@bot.on(
    events.NewMessage(pattern="^/help", func=lambda e: e.sender_id in SMEX_USERS)
)
async def ping(e):
    if e.sender_id in SMEX_USERS:
        text = "Opening Up Help Menu"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        await event.edit(f"❤️ Help Menu 💛\n/bigspam ~ ex-/bigspam 102 SpamBot\n/spam ~ ex/spam 10 hello\n/restart - To Restart Your App\n/ping - To Show Your Ping\n/raid - ex -/raid 10 Reply To Anyone's Message\n/replyraid ~ /replyraid Reply To Anyone's Message\n/dreplyraid ~ /dreplyraid Replt To Same Person To Stop Raid\n/update ~ To Update Your SpamBot")
