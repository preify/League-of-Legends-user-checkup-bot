import discord
import os
from discord import user
from discord import file
from riotwatcher import LolWatcher, ApiError
from discord.ext import commands
import io
import aiohttp



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
async def __lookup(ctx, arg1, arg2=''):
    try:
        code = lol_watcher.summoner.by_name(region[arg1.upper()], arg2)
        lookup_reply = discord.Embed(title=code['name'], description=f"Level {str(code['summonerLevel'])} \nIcon ID {str(code['profileIconId'])}")
        file = discord.File(f"C:/Users/Fjell/Documents/bot/media/12.1.1/img/profileicon/{str(code['profileIconId'])}.png", filename=str(code['profileIconId']))
        lookup_reply.set_thumbnail(url=f"attachment://{str(code['profileIconId'])}.png")
        await ctx.send(embed = lookup_reply)
    except KeyError:
        arg2 = "EUW1"
        code = lol_watcher.summoner.by_name(arg2, arg1)
        lookup_reply = discord.Embed(title=code['name'], description='%a \n' % code['summonerLevel']) 
        await ctx.send(embed = lookup_reply)

@bot.command(name='icon')
async def __icon(ctx, arg):
    await ctx.send('https://ddragon.leagueoflegends.com/cdn/10.18.1/img/profileicon/' + arg + '.png')

@bot.command(name='test')
async def __test(ctx, arg):
    try:    
        file = discord.File(f"C:/Users/Fjell/Documents/bot/media/12.1.1/img/profileicon/{arg}.png")
        await ctx.send(file=file)
    except:
        await ctx.send('No such Profile Icon ID number')


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
