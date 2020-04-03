from bs4 import BeautifulSoup
from requests import get
from urllib.parse import quote_plus
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN
from userbot.utils import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd("getmagnet (.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    result = ""
    if input_str:
        got = input_str
    else:
        await event.edit("Enter the torrent name you noob!")
        return
    got = got.split(";")
    query = got[0]
    selector = int(got[1])
    query = quote_plus(query)
    URL = (f"https://1337x.to/search/{query}/1/")
    page_src = get(URL, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"})
    soup = BeautifulSoup(page_src.text,"html.parser")
    name_value = soup.find_all("td",{"class":"coll-1 name"})
    a_value = name_value[selector-1].select("a")
    next_page = a_value[1].get("href")
    URL2=(f"https://1337x.to{next_page}")
    page2_src = get(URL2)
    soup2 = BeautifulSoup(page2_src.text,"html.parser")
    name = soup2.find("div", {"class":"col-9 page-content"}).find("h1").text
    magnet_link= soup2.find("div", {"class":"col-9 page-content"}).find("li").find("a").get("href")
    result = f"Name: {name}\n"+"Magnet Link: "+f"`{magnet_link}`\n"
    await event.edit(result)
