import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

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

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

bot.run("MTAxNzI0MjY4MDY4MzY2NzU0OA.GTHl3Z.UH2YhGPDcDBbYnqXmWCDNDSI_9JIw5rHojMYSQ")