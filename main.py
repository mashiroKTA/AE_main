import mysql.connector
import discord  #IMPORT DISCORD LIBRARY
from discord.ext import commands # IMPORT COMMANDS FROM DISCORD.EXT LIBRARY
import os
import time
import json



bot = commands.Bot(command_prefix='!') # THE PREFIX OF THE BOT
os.chdir(r'C:\Users\mashiro\Desktop\discord_bot\AEBot')
#-------------------------
# OPEN {MEMBERS ID..}
#-------------------------

KURAYAMI = 589017871431106561   # KURAYAMI ID

#------------------------
# END {MEMBERS ID..}
#------------------------

#--------------------------
#--------------------------
#--------------------------
#--------------------------

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

#--------------------------
#--------------------------
#--------------------------
#--------------------------


#--------------------------
# OPEN {when the bot is ready}
#--------------------------

@bot.event

async def on_ready():

    print(f'bot is ready')  # PRINT 'BOT IS READY 

#--------------------------
# END {when the bot is ready}
#--------------------------

#--------------------------
#--------------------------
#--------------------------
#--------------------------


#--------------------------
# OPEN {add auto role to member when he join}
#--------------------------


@bot.event

async def on_member_join(member):

    OFF_ROLE = discord.utils.get(member.guild.roles, id=int(OFF))
    await member.add_roles(OFF_ROLE)
    print(f'{member} has given {OFF_ROLE}')


# -----------------------------------------


#--------------------------
# END {add auto role to member when he join}
#--------------------------


#------------------------
# open {laod extension}
#------------------------

@bot.command()

async def dm(ctx):
    await ctx.send('this is dm')




@bot.command()

async def load(ctx, extension):

    if ctx.author.id == KURAYAMI:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{ctx.author.mention} loaded {ctx}')
    
    else:
        await ctx.send(f'{ctx.author.mention}\nERROR : انت لا تملك الصلاحيات ل تشغيلها')


#---------------------
# END {load extension}
#---------------------

#--------------------
#--------------------
#--------------------
#--------------------

#---------------------
# OPEN {unload extension}
#---------------------

@bot.command()

async def unload(ctx, extension):

    if ctx.author.id == KURAYAMI:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{ctx.author.mention} unloaded {ctx}')
    else:
        await ctx.send(f'{ctx.author.mention}\nERROR : انت لا تملك الصلاحيات ل اقافها')

#---------------------
# END {unload extension}
#---------------------

#---------------------
#---------------------
#---------------------
#---------------------


@bot.command()

async def reload(ctx, extension):

    if ctx.author.id == KURAYAMI:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'reloading....')
        time.sleep(3)
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{ctx.author.mention} reloaded {ctx}')

    else:
        await ctx.send(f'{ctx.author.mention}\nERROR : انت لا تملك الصلاحيات ل اعادة التشغيل')
        

#---------------------
# OPEN {import python files}
#---------------------


for filename in os.listdir(f'./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#---------------------
# END {import python files}
#---------------------










#DATABASES [ LEVEL SYSTEM (YOL)..  ]{
    










# }

bot.run('NjgxODUzNzM5OTc1NDQyNDQ2.XlUf3g.Lz_hUDXYRFSECoaxt3xMlHZvNew')      # RUN THE BOT
