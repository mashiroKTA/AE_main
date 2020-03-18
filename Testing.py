

import discord
from discord.ext import commands
import webbrowser


class Test(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    
    KURAYAMI = 589017871431106561

    @commands.command()
    

    async def SPAM(self, ctx, *, amount=None):

        KURAYAMI = 589017871431106561

        if (ctx.author.id) == KURAYAMI:

            if amount == None:

                await ctx.send(f'AMOUNT?')

            else:

                num = 1
                while num <= int(amount):

                    await ctx.send(f'''
                    
                    {ctx.author} -  `{num}` : `{str(amount)}`
                    
                    ''')

                    num += 1

        else:

            await ctx.send(f'only the tester can use this command')

    
    
    


def setup(bot):

    bot.add_cog(Test(bot))