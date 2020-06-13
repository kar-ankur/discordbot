import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client= commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send('hello')

@client.command()
async def game(ctx):
    game=['R6S','VALORANT','GTA5','skribblio','fortnite','CSGO','dead by daylight','chess','business','']
    await ctx.send(random.choice(game))   


client.run(TOKEN)
