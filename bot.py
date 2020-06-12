import discord

client= discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

client.run('NzIwODgyNTg0NjA2OTk4NjMw.XuMfmA.GfdLL0cHQT03qNsg4BUKiLQJx1o')
