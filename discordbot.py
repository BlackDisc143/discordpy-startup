#from discord.ext import commands
import discord
import os
import traceback

#bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = 'NjkzNDYwNjc1ODg3ODkwNDgy.Xn91Qg.4ktdCrdwz4aDL7PChqLD78X9AmA'

#@bot.command()
#async def chinato(ctx):
#    await ctx.send('私はチナトです。')
#    
#@bot.command()
#async def sakebu(ctx):
#    await ctx.send('Pythonわかんないいいいいいいいいいいいいいいいいいいいいいいいいいいいいい')
#    
#bot.run(token)

@client.event
async def on_message(message):
    if message.content == '/chinato':
        if client.user != message.author:
            await message.channel.send('チナトです。')

client.run("token")
