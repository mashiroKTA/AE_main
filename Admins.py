

import discord
from discord.ext import commands

#--------------------------
# OEPN {ROLES ID..}
#--------------------------


OFF = 680856221611458630    # OFF ROLE ID
ADMIN = 680843267096838165      # 'مشرف' ROLE ID
MEMBER = 680853336593137755     # "عضو" ROLE ID
DBOT = 681106839030595597       # "DBOT" ROLE ID
PROGRAMMER = 680843495413514277     #"مبرمج السيرفر" ROLE ID

#--------------------------
# END {ROLES ID..}
#--------------------------


class Admin(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is ready')




#------------------------
# OPEM {remove Roles to members}
#------------------------

    @commands.command()
    @commands.has_role('مشرف')

    async def rmROLE_OFF(self, ctx, member:discord.Member):

        OFF_ROLE = discord.utils.get(member.guild.roles, id=int(OFF))
        await member.remove_roles(OFF_ROLE)
        await ctx.send(f'{member} has removed {OFF_ROLE}')
        print(f'{member} has removed {OFF_ROLE}')

    

    @commands.command()
    @commands.has_role('مشرف')

    async def rmROLE_MEMBER(self, ctx, member:discord.Member):

        MEMBER_ROLE = discord.utils.get(member.guild.roles, id=int(MEMBER))
        await member.remove_roles(MEMBER_ROLE)
        await ctx.send(f'{member} has removed {MEMBER_ROLE}')
        print(f'{member} has removed {MEMBER_ROLE}')





#------------------------
# END {remove Roles to members}
#------------------------


#------------------------
#------------------------
#------------------------
#------------------------

#------------------------
# OPEN {ADD ROLES TO MEMBERS}
#------------------------

    @commands.command()
    @commands.has_role('مشرف')

    async def addROLE_MEMBER(self, ctx, member:discord.Member):

        MEMBER_ROLE = discord.utils.get(member.guild.roles, id=int(MEMBER))
        await member.add_roles(MEMBER_ROLE)
        await ctx.send(f'{member} has given {MEMBER_ROLE}')
        print(f'{member} has given {MEMBER_ROLE}')

    
    @commands.command()
    @commands.has_role('مشرف')

    async def addROLE_OFF(self, ctx, member: discord.Member):

        OFF_ROLE = discord.utils.get(member.guild.roles, id=int(OFF))
        await member.add_roles(OFF_ROLE)
        await ctx.send(f'{member} has given {OFF_ROLE}')
        print(f'{member} has given {OFF_ROLE}')

    


#------------------------
# END {ADD ROLES TO MEMBER}
#------------------------

#------------------------
#------------------------
#------------------------
#------------------------

#------------------------
# OPEN {KICK SYSTEM}
#------------------------

    @commands.command()
    @commands.has_role('مشرف')
    async def kick(self, ctx, member:discord.Member):
        await member.kick()
        await ctx.send(f'{ctx.author.mention} Kicked {member.mention}')

    


#------------------------
# END (KICK SYSTEM)
#------------------------
 
    @commands.command()
    @commands.has_role('مشرف')
    async def ban(self, ctx, member:discord.Member):
        await member.ban()
        await ctx.send(f'{ctx.author.mention} Banned {member.mention}')

    


    @commands.command()
    @commands.has_role('مشرف')
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')


        for bans in banned_users:

            user = bans.user

            if (user.name,user.discriminator) == (member_name, member_discriminator):

                await ctx.guild.unban(user)
                await ctx.send(f'{ctx.author.mention} Unbanned {user.mention}')
                return




def setup(bot):

    bot.add_cog(Admin(bot))
