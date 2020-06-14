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
    game=['R6S','VALORANT','GTA5','skribblio','fortnite','CSGO','dead by daylight','chess','business']
    await ctx.send(random.choice(game))   

@client.command()
async def ping(ctx):
    await ctx.send('Pong!{}ms'.format(round(client.latency*1000)))

@client.command()
async def bangu(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/692472840922071050.png?v=1')

@client.command()
async def bala(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/694862322648219709.png?v=1')

@client.command()
async def ronit(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/692472718037352459.png?v=1')

@client.command()
async def tanmay(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/692386639489794058.png?v=1')

@client.command()
async def kade(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/692473080148262932.png?v=1')

@client.command()
async def mtg(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/696120065845624912.png?v=1')

@client.command()
async def kunal(ctx):
    await ctx.send('https://cdn.discordapp.com/emojis/696121633814872114.png?v=1')


client.run(TOKEN)
