import discord
import os
from discord import user
from requests.models import Response
from requests.sessions import PreparedRequest
from riotwatcher import LolWatcher, ApiError
from discord.ext import commands
from decouple import config


# ENV TABLE STUFF
os.environ.get('DISCORD_BOT_TOKEN')
os.environ.get('LEAGUE_API')

#LOL WATCHER STUFF
lol_watcher = LolWatcher(os.getenv('LEAGUE_API'))

#All regions 
region = {
    "EUW": "EUW1",
    "NA": "NA1",
    "BR": "BR1",
    "EUNE": "EUNE",
    "OCE": "OCE",
    "LAN": "LA1",
    "LAS": "LA2",
    "RU": "RU1",
    "TR": "TR1",
    "JP": "JP1",
    "KR": "KR",
    "PBE": "PBE",
}


#Prefix
bot = commands.Bot(command_prefix='$')

#Commands
@bot.event # Log-in check
async def on_ready():
    print('Logged in as user {0.user}'.format(bot))

@bot.command(name='lookup') # Command for checking league accounts 
async def __lookup(ctx, arg1, arg2):
    try:
        code = lol_watcher.summoner.by_name(region[arg1.upper()], arg2)
        lookup_reply = discord.Embed(title=code['name'], description='%a \n' % code['summonerLevel'] + 'Test mode') 
        await ctx.send(embed = lookup_reply)
    except KeyError:
        arg2 = region['EUW']
        code = lol_watcher.summoner.by_name(region[arg2], arg1)
        lookup_reply = discord.Embed(title=code['name'], description='%a \n' % code['summonerLevel'] + 'Test mode') 
        await ctx.send(embed = lookup_reply)





bot.run(os.getenv('DISCORD_BOT_TOKEN'))
