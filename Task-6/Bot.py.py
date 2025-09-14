import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')

@bot.command()
async def lyrics(ctx, *, song):
  url = f'https://api.lyrics.ovh/v1/{song}'
  r = requests.get(url)
  if r.status_code == 200:
    data = r.json()
    text = data.get('lyrics')
    if text:
      await ctx.send(text[:500]+'...')
    else:
      await ctx.send('No lyrics found')
  else:
    await ctx.send('Couldn\'t get lyrics')

bot.run('YMTQxNjc3ODkwNzk2NDkzMjI2OA.GWIBS4.ztUhOSR7M5DUOnOLKSajqjU8bfFfE8KecqN9Yg')

