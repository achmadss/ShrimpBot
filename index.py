import os
from discord.ext.commands import Bot
import sys


BOT_PREFIX = ("?")
TOKEN = os.getenv("DISCORD_TOKEN")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")

sys.path.append('/commands')

client.run(TOKEN)