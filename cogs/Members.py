

import discord
from discord.ext import commands



class Members(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is ready')

    @commands.command()
    @commands.has_role('عضو')
    async def ping(self, ctx):

        await ctx.send('PONG!!!')



def setup(bot):

    bot.add_cog(Members(bot))
