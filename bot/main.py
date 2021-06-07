import discord
import os
#import pynacl
#import dnspython
import server
import requests
from discord.ext import commands

client = commands.Bot(command_prefix='~')
client2 = discord.Client()
updatefunc = False


@client.command()
async def hex(ctx, member: discord.Member):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'hex', 'author': str(ctx.author), 'target': str(member)})
	await ctx.send(f'{str(member)} has been hexed!')
@client.event
async def on_ready():
    print("Bot is on")

@client.command()
async def bal(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'show_bal', 'author': str(ctx.author)})
	json_response = response.json()
	bal = json_response['money']
	await ctx.send(bal)


@client.command()
async def select_pistol(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'pistol', 'ammo':'pistol_bul'})
	json_response = response.json()
	if json_response['weapon'] == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
	if json_response['ammo_ammount'] == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {json_response['ammo_ammount'} arrows')
 
    
@client.command()
async def select_rifle(ctx):
    	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'rifle', 'ammo':'rifle_bul'})
	json_response = response.json()
	if json_response['weapon'] == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
	if json_response['ammo_ammount'] == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {json_response['ammo_ammount'} arrows')
 
   

@client.command()
async def select_flame(ctx):
    	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'flame', 'ammo':'propane'})
	json_response = response.json()
	if json_response['weapon'] == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
	if json_response['ammo_ammount'] == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {json_response['ammo_ammount'} arrows')
 

@client.command()
async def select_bow(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'bow_and_arrow', 'ammo':'arrows'})
	json_response = response.json()
	if json_response['weapon'] == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
	if json_response['ammo_ammount'] == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {json_response['ammo_ammount'} arrows')
    #Bot will say: @user select bow
   

@client.command()
async def select(ctx):
    await ctx.send("Weapon commands available: select_bow, select_flame, select_rifle, select_pistol")
    
@client.command(pass_context=True)
async def say(ctx, *, messages):
	await ctx.send(messages)


TOKEN = os.getenv("DISCORD_TOKEN")
server.server()
client.run(TOKEN)
