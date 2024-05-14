import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready")

@client.command
async def ping(ctx):
    await ctx.send("Pong!")


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)