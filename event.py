import discord
import audioop
# $ pip install audioop-lts

from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())
# En résumé, ce code initialise un client Discord avec toutes les intentions activées, ce qui permet au bot de recevoir et de réagir à tous les événements possibles sur Discord.

# gerer plusieurs tâche en meme temps sans se bloquer 

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    # voir si ton message commence par bonjour // et le bot repond uniquement si tu dis bonjour
    elif message.content.lower().startswith("bonjour"): 
        await message.channel.send("Bonjour, c'est le bot")         
        


@client.event
async def on_message_delete(message: discord.Message):
    await message.channel.send(f"{message.author.name} a supprimé {message.content}")
    #permet de voir le contenu du message supprimé envoyé de l'utilisateur 
  


@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    await after.channel.send(f"{before.author.name} {after.content}")
    # l'ancien message est devenu le nouveau message 
  
@client.event 
async def on_ready():
    print("Le bot est prêt")
    
    
     

client.run(token=token)

 
