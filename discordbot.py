from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def chinato(ctx):
    await ctx.send('私はチナトです。')
    
@bot.command()
async def sakebu(ctx):
    await ctx.send('Pythonわかんないいいいいいいいいいいいいいいいいいいいいいいいいいいいいい')
    
@bot.event
async def on_message(message):
    if message == 'hoge':
        await ctx.send('hage')

bot.run(token)
