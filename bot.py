import discord
from discord.ext import commands

intents=discord.Intents.default()

bot = commands.Bot(command_prefix='#',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")    

bot.run("MTAxNzI0MjY4MDY4MzY2NzU0OA.GpBFul.IkL4NTapQ6S0164ObpONHqV8aPX9mD3rVaeEgg")