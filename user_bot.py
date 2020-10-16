import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="_") # CHANGEABLE PREFIX
channels = [765346710435266581, 755769922289664060, 754869146453278856, 761914882635202640, 758379429964546080, 764561567143559178, 765273000995848282, 760409070829174794]
bot.remove_command('help')


@bot.event
async def on_message(message):
  if message.channel.type == discord.ChannelType.private:
    if message.author == bot.user:
      return
    else:
      await message.channel.send("https://discord.gg/B8P67d")  # Link of Army Town
      armyTownChannel = bot.get_channel(765229524349747231)
      await armyTownChannel.send(f"I sent invite to {message.author.name}")
  else:
    pass

@bot.event
async def on_ready():
  while True:
    for ch in channels:
      channel = bot.get_channel(ch)
      await channel.send("DM for j4j")
    await bot.change_presence(status=discord.Status.invisible)
    await asyncio.sleep(7200)

@bot.command()
async def checkuser(ctx):
  await ctx.send(f"{ctx.message.author.mention} I am alive, till now..........")

bot.run("NzE4NzA2NTExNDMzNDMzMTA4.X4h-oQ.nbQS6Xm1GpxZKVQMckCLsysBQrc", bot=False) # TOKEN