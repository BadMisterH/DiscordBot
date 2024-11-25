import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command(name="bonjour_monde", aliases=['hw', 'hellow_word'])
async def hello_world(context):
    await context.send("Hello, World!")
    
@bot.command()
async def decompte(context, delai: int):
    await context.send("Départ dans ...")
    for i in range(delai, 0, -1):
        await context.send(i)
    await context.send("c'est parti")
    
@bot.command(
    description="Repète du texte qu'on lui passe",
    brief= "Répéte du texte",
    help= "Encore plus d'aide"
)
# '*'  ce symbole permet de prendre le contenu de tout le message si dans ce message il y a des espaces 
async def repeter(context, *, message):
    await context.send(message)

if __name__ == '__main__':
    bot.run(token=token)
    