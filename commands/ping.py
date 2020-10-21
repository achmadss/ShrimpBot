import random as random

@client.command()
async def ping(context):
    res = [
        "OK peko~",
        "Konpeko~",
        "ogey~"
    ]
    await context.send(random.choice(res) + " " + context.message.author.mention)