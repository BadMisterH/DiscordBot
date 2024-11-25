import discord
import audioop
# $ pip install audioop-lts

from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connecté en tant que {client.user}")

client.run(token)


