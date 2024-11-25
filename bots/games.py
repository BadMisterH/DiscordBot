import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command()
async def roll(ctx):
    result = random.randint(1, 6)
    await ctx.send(f'{ctx.author.name} a lancé le dé : {result}')

@bot.command()
async def pileouface(ctx):
    result = random.choice(['pile', 'face'])
    await ctx.send(f'Résultat obtenu : {result}')

@bot.event
async def on_ready():
    await bot.tree.sync()
    
bot.run(token)
