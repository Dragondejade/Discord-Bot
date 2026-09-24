import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()


print("Lancement du bot ...")
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    #syncro les commandes
    print("Bot allumé !")

    try:
        synced = await bot.tree.sync()
        print(f"Commande slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message : discord.Message):
    if message.author.bot:
        return

    if message.content.lower() == 'bonjour':
        channel = message.channel
        author = message.author
        await author.send("Comment tu vas ?")

@bot.tree.command(name="secret", description="A tes risque et périls !")
async def secret(interaction : discord.Interaction):
    await interaction.response.send_message("Voici le secret : https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")

#@bot.tree.command(name="test", description="Tester les embeds")
async def test(interaction : discord.Interaction):
    embed = discord.Embed(
    title ="Test Title",
    description="Description de l'embed",
    color=discord.Color.blue()
    )
    embed.add_field(name="Truc", value="Affiche truc")
    embed.add_field(name="Machin", value="Affiche machin")

    await interaction.response.send_message(embed=embed)

#@bot.tree.command(name="warnguy", description="Averti une personne")
async def warnguy(interaction : discord.Interaction, member : discord.Member):
    await interaction.response.send_message("Alerte envoyé !")
    await member.send("Tu as reçu une alerte")

#@bot.tree.command(name="banguy", description="Ban une personne")
async def banguy(interaction : discord.Interaction, member : discord.Member):
    await member.ban("Vous ne respectiez pas les règles")
    await member.send("Tu as reçu une alerte")

bot.run(os.getenv('DISCORD_TOKEN'))