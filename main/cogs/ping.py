import discord
from discord.ext import commands

class pingcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping', help='Replies with pong!')
    async def hello(self, ctx):
        await ctx.send(f'Pong!')

def setup(bot):
    bot.add_cog(pingcommand(bot))
