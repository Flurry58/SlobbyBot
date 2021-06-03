import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

client = commands.Bot(command_prefix='&')
client2 = discord.Client()
updatefunc = False



@client.event
async def on_ready():
    print("Bot is on")

#@client.command()
#async def bal(ctx):
    #Shows @users Bal
   

#@client.command()
#async def select_gun(ctx):
    #Bot will say: @user select gun
    
#@client.command()
async def select_rifle(ctx):
    #Bot will say: @user select rifle
   

#@client.command()
#async def select_flame(ctx):
    #Bot will say: @user select flamethrower
 

#@client.command()
#async def select_bow(ctx):
    #Bot will say: @user select bow
   

#@client.command()
#async def select(ctx):
    #Bot will say: The types of weapons are crossbow, gun, rifle, speaker, and flame
    
@client.command(pass_conetext=True)
async def say(ctx, *, messages):
	await ctx.send(messages)


TOKEN = os.getenv("DISCORD_TOKEN")
server.server()
client.run(TOKEN)
