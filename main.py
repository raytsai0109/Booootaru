import discord
import os
import keep_alive
import random
import json

from discord.ext import commands

activity = discord.Activity(type=discord.ActivityType.watching, name="21點到底怎麼玩")
pasw = os.environ['Password']
client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), activity=activity, status=discord.Status('online'))


@client.event
async def on_ready():
    print("Bot is online")

@client.command()
async def secret(ctx,msg):
  with open("things.json","r") as f:
    users= json.load(f)
  num = users['anony']
  users['anony']+=1
  with open("things.json","w") as f:
    users= json.dump(users,f)
  channel = client.get_channel(935346685436121158)
  embed=discord.Embed(title=f'#{num}', color=0x31b120)
  embed.set_author(name="匿名發言")
  embed.set_footer(text=f'{msg}')
  await channel.send(embed=embed)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    keep_alive.keep_alive()
    client.run(pasw)
