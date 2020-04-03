from bs4 import BeautifulSoup
from requests import get
from urllib.parse import quote_plus
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN
from userbot.utils import register
from userbot.utils import admin_cmd


@borg.on(admin_cmd("torlist (.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        query = input_str
    else:
        await event.edit("Enter the torrent name you noob!")
        return
    query = quote_plus(query)
    URL = (f"https://1337x.to/search/{query}/1/")
    await event.edit("Fetching data...")
    page_src = get(URL, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    soup = BeautifulSoup(page_src.text,"html.parser")
    name_value = soup.find_all("td",{"class":"coll-1 name"})
    seed_value = soup.find_all("td",{"class":"coll-2 seeds"})
    leech_value = soup.find_all("td",{"class":"coll-3 leeches"})
    result = ""
    f_result = ""
    for i in range(10):
        a_value = name_value[i].select("a")
        name = a_value[1].text
        seeders = seed_value[i].text
        leechers = leech_value[i].text
        result = f"{i+1}) Name: {name}\nSeeders: {seeders}\nLeechers: {leechers}\n"
        f_result = f_result+result
    await event.edit(f_result)

