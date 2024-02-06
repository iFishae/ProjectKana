# Project Kana


# Main Imports
import discord
from discord.ext import commands
import openai
import mysql
import os
from dotenv import load_dotenv

# Processing enviromental variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPEN_AI_KEY')

# For a MySQL database.
# MYSQL_HOST = os.getenv('MYSQL_HOST')
# MYSQL_PORT = os.getenv('MYSQL_PORT')
# MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')


# Required Discord Intents
intents = discord.Intents.default()

# Main
bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in!')
    bot.load_extension('cogs.pingcommand')

@bot.event
async def on_message(message):
    # Ignores messages sent by the bot itself.
    if message.author.id == '1202990932589281280':
        return


bot.run(DISCORD_TOKEN)
