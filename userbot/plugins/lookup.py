from requests import get
from userbot.utils import admin_cmd
import json
@borg.on(admin_cmd("bin (.*)"))
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
        name = data.get("bank",{}).get("name"," ")
        scheme = data.get("scheme"," ")
        typ = data.get("type"," ")
        brand = data.get("brand"," ")
        country = data.get("country",{}).get("name"," ")
        await event.edit(f"BIN: {BIN}\nName: {name}\nScheme: {scheme}\nType: {typ}\nBrand: {brand}\nCountry: {country}")
    except:
        await event.edit(f"{BIN} is Invalid BIN")
    
