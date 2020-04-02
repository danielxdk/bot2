""" techrimail scraper plugin by @scifidemon """

import os

from bs4 import BeautifulSoup

import re

from time import sleep

import re

from datetime import datetime

from requests import get

from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN

from userbot.utils import register

from userbot.utils import admin_cmd


@borg.on(admin_cmd("getmail (.*)"))
async def _(event):
    address=""
    fresult=""
    result=""
    result1=""
    result2=""
    input_str = event.pattern_match.group(1)
    if input_str:
        address = input_str
    else:
        await event.edit("Enter an address you noob!")
        return
    await event.edit("`Retrieving the last 5 emails....`")
    URL = f"https://techrimail.herokuapp.com/{address}@t.techrim.tech"
    page_src = get(URL)
    soup = BeautifulSoup(page_src.text,"html.parser")
    emails = soup.find_all("blockquote",{"class":"email"})
    for i,email in enumerate(emails):
        sender = email.find("h6").text
        subject = email.find("p").text
        sender = os.linesep.join([s for s in sender.splitlines() if s])
        subject = os.linesep.join([s for s in subject.splitlines() if s])
        result1 = f"{i+1}) Sender/Date:\n{re.sub(' +',' ',sender)}\n"
        result2 = f"Subject:\n{re.sub(' +',' ',subject)}\n\n"
        result = result1+result2
        fresult = fresult+result
        if i==4:
            break
    await event.edit(fresult)
