from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    await ctx.send('起動を確認したよ')

@bot.command()
async def chinato(ctx):
    await ctx.send('私はチナトです。')
    
@bot.command()
async def sakebu(ctx):
    await ctx.send('Pythonわかんないいいいいいいいいいいいいいいいいいいいいいいいいいいいいい')
    
@bot.event
async def on_member_update(before, after):
    if before.status != after.status:
        msg = after.display_name + " さんが " + str(after.status) + " になりました"
        await client.send_message(text_chat,msg)

bot.run(token)
