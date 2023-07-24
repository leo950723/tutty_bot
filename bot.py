import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True
bot = commands.Bot(command_prefix='#',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(1133085871999045753)
    await channel.send(f'{member} join')
@bot.event
async def on_member_remvoe(member):
    channel=bot.get_channel(1133086140681953412)
    await channel.send(f'{member} leave')

bot.run("MTAxNzI0MjY4MDY4MzY2NzU0OA.GYufq1.lDz61KHQ9TmAJdl0z5JvMeEv4FbPZn3h8nS4Ao")