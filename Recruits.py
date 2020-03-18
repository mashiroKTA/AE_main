import discord
from discord.ext import commands


class Recruits(commands.Cog):

    def __init__(self, bot):

        self.bot = bot





    @commands.command()
    @commands.has_role('Recruit')
    
    async def T(self, ctx):

        
        await ctx.send(f'''


:dagger::shield:Ánîmè:crossed_swords:Émpîrè:shield::dagger:

:bell:~اعلان~:bell:

:trident:~نوع الاعلان~:trident:    :

:jigsaw:~عدد الاسئلة~:jigsaw:    :

:trophy:~نوع الاسئلة~:trophy:   :

:clapper:~الانميات~:clapper:    :

:date:~اليوم~:date:    :

:clock330:~التوقيت~:clock9:    :

:red_envelope:~المقدم~:red_envelope:    :

Ⓐ𝒏𝒊𝒎𝒆 Ⓔ𝒎𝒑𝒊𝒓𝒆



        ''')


    @commands.command()
    @commands.has_role('Recruit')


    async def Slink(self, ctx):

        await ctx.send('https://discord.gg/56UvJH')


    



def setup(bot):

    bot.add_cog(Recruits(bot))