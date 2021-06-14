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
async def testing(ctx):
	await ctx.send("SlobbyBot is on and working")

@client.command()
async def attack(ctx, weapon, member: discord.Member):
	requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'update', 'author': str(member)})
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'attack', 'author': str(ctx.author), 'target': str(member)})
	json_response = response.json()
	health = json_response['response']
	health2 = health['health']
	if json_response['yes'] == 1:
		await ctx.send(f'The targets health is now at {health2}!')
	else:
		await ctx.send(json_response['response'])
									
										

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
	ammo = json_response['ammo_ammount']
	weapon_status = json_response['weapon']
	if weapon_status == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
		await ctx.send("Pistol has been selected")
	if ammo == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {ammo} pistol bullets')
 
    
@client.command()
async def select_rifle(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'rifle', 'ammo':'rifle_bul'})
	json_response = response.json()
	ammo = json_response['ammo_ammount']
	weapon_status = json_response['weapon']
	if weapon_status == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
		await ctx.send("Rifle has been selected")
	if ammo == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {ammo} rifle bullets')
 
   

@client.command()
async def select_flame(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'flame', 'ammo':'propane'})
	json_response = response.json()
	ammo = json_response['ammo_ammount']
	weapon_status = json_response['weapon']
	if weapon_status == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
		await ctx.send("Flamethrower has been selected")
	if ammo == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {ammo} propane')
 
 

@client.command()
async def select_bow(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'select_weapon', 'author': str(ctx.author), 'weapon': 'bow_and_arrow', 'ammo':'arrows'})
	json_response = response.json()
	ammo = json_response['ammo_ammount']
	weapon_status = json_response['weapon']
	if weapon_status == 0:
		await ctx.send("you don't have this weapon")
	else:
		await ctx.send("You have this weapon")
		await ctx.send("Bow and Arrow has been selected")
	if ammo == 0:
		await ctx.send("you don't have any ammo for this weapon!")
	else:
		await ctx.send(f'you have {ammo} arrows')

@client.command()
async def buy(ctx, *, item_name, amount):
	await ctx.send("coming soon")
@client.command()
async def show_shop(ctx):
	embed = discord.Embed(title="Items Available", color=0xff00f6) 
    	await ctx.send(embed=embed)
	embed = discord.Embed(title="🍻Bar Membership", description="Buy a membership and treat yourself to some of the best beers in town -- Price: 100,000", color=0x1f85de)
	await ctx.send(embed=embed)
	embed = discord.Embed(title="🍺Beer", description="Order a nice refreshing Stein of beer -- Price: 10,000", color=0x1f85de)
	await ctx.send(embed=embed)
	embed = discord.Embed(title="💵Nine Thousand Dollars", description="Don't like your beer? You can sell it back to us for a 90% refund -- Price: 🍺1", color=0x1f85de)
	await ctx.send(embed=embed)
	embed = discord.Embed(title="🏹Crossbow", description="Don't like your beer? You can sell it back to us for a 90% refund -- Price: 🍺1", color=0x1f85de)
	await ctx.send(embed=embed)
	
@client.command()
async def select(ctx):
    await ctx.send("Weapon commands available: select_bow, select_flame, select_rifle, select_pistol")
    
@client.command(pass_context=True)
async def say(ctx):
	response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'health_restart'})


TOKEN = os.getenv("DISCORD_TOKEN")
server.server()
client.run(TOKEN)
