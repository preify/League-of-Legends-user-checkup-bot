import discord
import os
from discord import user
from riotwatcher import LolWatcher, ApiError
from discord.ext import commands
from decouple import config


# ENV TABLE STUFF
os.environ.get('DISCORD_BOT_TOKEN')
os.environ.get('LEAGUE_API')

#LOL WATCHER STUFF
lol_watcher = LolWatcher(os.getenv('LEAGUE_API'))
region1 = 'euw1'

#Prefix
bot = commands.Bot(command_prefix='%')

#Commands
@bot.event # Log-in check
async def on_ready():
    print('Logged in as user {0.user}'.format(bot))

@bot.event # Placeholder
async def on_message(message):
    if message.author == bot.user:
        return

@bot.command() # Command for checking league accounts 
async def league():
    pass
    
    


    
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
