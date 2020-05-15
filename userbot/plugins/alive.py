"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet... puk you"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("Corona hasn't killed me yet.\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3`\n"
                     "`Database Status: Databases functioning normally!(unless you run out of dynos)`\n"
                     f"`This nibba my boss: {DEFAULTUSER}`\n")
