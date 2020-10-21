import random as random, discord
from discord.ext import commands

# ini class Basic
# nanti di help ada kategori "Basic"
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command ping
    @commands.command()
    async def ping(self, context):
        res = [
            "OK peko~",
            "Konpeko~",
            "ogey~"
        ]
        await context.send(random.choice(res) + " " + context.message.author.mention)

    # command slap
    @commands.command()
    async def slap(self, context):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await context.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Basic(bot))    