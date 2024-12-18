import discord
from discord.ext import commands

file = open("key.txt", 'r')
TOKEN = file.read()

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("-------------")
    print("    ready    ")
    print("-------------")

@client.command()
async def hello(ctx):
    await ctx.send("hello")

client.run(TOKEN)