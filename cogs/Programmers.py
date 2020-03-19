

import discord
from discord.ext import commands


class Programmers(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


#----------------
# OPEN {DELETE SOME MESSAGES}
#----------------

    @commands.command()
    @commands.has_role('مبرمج السيرفر')

    async def purge(self, ctx, *,amount=None):

        i = 'all'

        if amount == None:
            await ctx.send('AMOUNT?')

        elif amount == i:
            await ctx.channel.purge(limit=int(1000000000))

        else:
            await ctx.channel.purge(limit=int(amount))

    


    
#----------------
# END {DELETE SOME MESSAGES}
#----------------



def setup(bot):

    bot.add_cog(Programmers(bot))