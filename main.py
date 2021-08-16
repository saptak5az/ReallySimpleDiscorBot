import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_start():
  print("Bot is online")

@bot.command()
async def hello(ctx):
  await ctx.send ("Hello")

token=("TOKEN") # delete the word TOKEN and paste your token here
bot.run(token)