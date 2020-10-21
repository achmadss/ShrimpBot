import random as random
from discord.ext import commands

# ini class Basic
# nanti di help ada kategori "Basic"
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ini command ping
    @commands.command()
    async def ping(self, context):
        res = [
            "OK peko~",
            "Konpeko~",
            "ogey~"
        ]
        await context.send(random.choice(res) + " " + context.message.author.mention)




def setup(bot):
    bot.add_cog(Basic(bot))    