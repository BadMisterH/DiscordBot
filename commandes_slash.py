import discord
from discord.ext import commands
from discord import app_commands
import time
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Configuration du bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Commande slash : multiplication
@bot.tree.command(name="multiplication", description="Multiplie deux nombres.")
async def multiplication(interaction: discord.Interaction, a: int, b: int):
    await interaction.response.send_message(f"{a} * {b} = {a * b}")
    
    
@bot.tree.command()
async def repete(interaction: discord.Integration, nombre:int, message:str):
    await interaction.response.send_message(message)
    for _ in range(1, nombre):
        await interaction.followup.send(message)
        
@bot.tree.command()
async def attends(interaction: discord.Interaction, secondes : int):
    await interaction.response.defer()
    time.sleep(secondes)
    await interaction.followup.send("J'ai fini")
    

# Événement lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisé(s)")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")

# Fonction principale pour démarrer le bot
def main():
    bot.run(token)

if __name__ == '__main__':
    main()
