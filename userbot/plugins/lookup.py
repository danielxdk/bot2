from requests import get
from userbot.utils import admin_cmd
import json
@borg.on(admin_cmd("lookup (.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        BIN = input_str[:6]
    else:
        await event.edit("No BIN entered!")
        return
    URL = f"https://lookup.binlist.net/{BIN}"
    await event.edit("Looking Up the BIN...")
    try:
        data = get(URL).json()
        name = data["bank"]["name"]
        scheme = data["scheme"]
        typ = data["type"]
        brand = data["brand"]
        country = data["country"]["name"]
        await event.edit(f"Name: {name}\nScheme: {scheme}\nType: {typ}\nBrand: {brand}\nCountry: {country}")
    except:
        await event.edit("Invalid BIN")
    