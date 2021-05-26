import discord
import os
import requests
#import pynacl
#import dnspython
import server
from discord.ext import commands

bot = commands.Bot(command_prefix="~")
TOKEN = os.getenv("DISCORD_TOKEN")
URL = "https://KnobbyConcernedTitle.loganpollack.repl.co"

@bot.event
async def on_ready():
    pload = {'username':'olivia','password':'123'}
    r = requests.post('https://httpbin.org/post',data = pload)
    print(r.json())
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def bal(ctx):
    #Shows @users Bal
    pass

@bot.command()
async def select_gun(ctx):
    #Bot will say: @user select gun
    pass

@bot.command()
async def select_rifle(ctx):
    #Bot will say: @user select rifle
    pass

@bot.command()
async def select_flame(ctx):
    #Bot will say: @user select flamethrower
    pass

@bot.command()
async def select_bow(ctx):
    #Bot will say: @user select bow
    pass

@bot.command()
async def select(ctx):
    #Bot will say: The types of weapons are crossbow, gun, rifle, speaker, and flame
    pass



server.server()
bot.run(TOKEN)
