import os, glob
import random as random
from discord.ext.commands import Bot
from .commands import *

commands = []
os.chdir("/commands")
for file in glob.glob("*.py"):
    commands.append(file)

BOT_PREFIX = ("?")
TOKEN = os.getenv("DISCORD_TOKEN")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}({client.user.id})")

@client.command()
async def ping(context):
    # res = [
    #     "OK peko~",
    #     "Konpeko~",
    #     "ogey~"
    # ]
    # await context.send(random.choice(res) + " " + context.message.author.mention)
    await context.send(commands[0])

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startsWith(BOT_PREFIX):
#         command = message.content.split(None, 1)[0]
#         if command == 

client.run(TOKEN)