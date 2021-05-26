import discord
import os
import json
#import pynacl
#import dnspython
import server
from discord.ext import commands
updatefunc = False
bot = commands.Bot(command_prefix="~")
TOKEN = os.getenv("DISCORD_TOKEN")
URL = "https://KnobbyConcernedTitle.loganpollack.repl.co"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def bal(ctx):
    #Shows @users Bal
    pass

async def update_data(users, auth):
  if not f'{auth}' in users:
        users[f'{auth}'] = {}
        users[f'{auth}']["bal"] = 0
        users[f"{auth}"]["goose"] = 0
        users[f"{auth}"]["goosestats"] = {}
        users[f"{auth}"]["goosestats"]["kills"] = 0
        users[f"{auth}"]["goosestats"]["power"] = 0                
        users[f"{auth}"]["arrows"] = 0
        users[f"{auth}"]["bow_and_arrow"] = 0
        users[f"{auth}"]["propane"] = 0
        users[f"{auth}"]["flame"] = 0
        users[f"{auth}"]["rifle_bul"] = 0
        users[f"{auth}"]["rifle"] = 0
        users[f"{auth}"]["pistol"] = 0
        users[f"{auth}"]["pistol_bul"] = 0
        users[f"{auth}"]["speaker"] = 0
        updatefunc = True
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

@bot.event
async def on_message(message):
    with open('bot/data.json', 'r') as f:
      users = json.load(f)
      await update_data(users, str(message.author))
      with open('bot/data.json', 'w') as f:
        json.dump(users, f)
    
    await bot.process_commands(message)


server.server()
bot.run(TOKEN)
