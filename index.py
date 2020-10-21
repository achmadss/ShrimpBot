import random as random
from discord.ext.commands import Bot

BOT_PREFIX = ("?")
TOKEN = "NzY4NDA1ODc3ODQ1NTI0NDgx.X4__vQ.zAh8X7eJyD63g3LtBpdTkfO-llI"

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def ping(context):
    res = [
        "OK peko~",
        "Konpeko~",
        "ogey~"
    ]
    await context.send(random.choice(res) + " " + context.message.author.mention)



client.run(TOKEN)