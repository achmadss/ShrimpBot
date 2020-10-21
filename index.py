import os
import random as random
from discord.ext.commands import Bot

BOT_PREFIX = ("?")
TOKEN = os.getenv("DISCORD_TOKEN")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")

@client.command()
async def ping(context):
    res = [
        "OK peko~",
        "Konpeko~",
        "ogey~"
    ]
    await context.send(random.choice(res) + " " + context.message.author.mention)



client.run(TOKEN)