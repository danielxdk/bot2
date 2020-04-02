""" CC checker userbot plugin coded by @scifidemon and API by @Dr34m_C4t """
from telethon import events, errors, functions, types
import inspect
import traceback
import asyncio
import sys
import io
import json
from requests import get

@command(pattern="^.cc")
async def _(event):
    if event.fwd_from:
        return
    cclist = event.text.split(" ")
    n = len(cclist)
    await event.edit("Checking...")
    final_result=""
    for i in range(1,n):
        cc = cclist[i]
        URL = f"https://api.validcc.pro/?key=r21NZ5AODUqL101hPNeN&cc={cc}"
        r = get(URL).json()
        code = f"Code: {r['code']}\n"
        status = f"Status: {r['status']}\n"
        card = "Card: "+ f"`{r['card']}`\n"
        rem_req = f"Remaining requests: {r['requests_remaining']}\n"
        result = code+status+card+rem_req
        final_result = final_result+result
        await event.edit(final_result+"Checking more...")
    await event.edit(final_result+"DONE CHECKING!!!")
        




