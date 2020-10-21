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
    async def slap(self, context, member: discord.Member):
        await context.send(f"PONG {member}")
        # embedVar = discord.Embed(title=context.message.author.mention+" ", description="", color=0x00FFFF)
        # embedVar.add_field(name="Field1", value="hi", inline=True)
        # embedVar.add_field(name="Field2", value="hi2", inline=False)
        # await context.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Basic(bot))    