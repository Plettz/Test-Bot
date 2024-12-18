import discord
from discord.ext import commands

file = open("key.txt", 'r')
TOKEN = file.read()
print(TOKEN)

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("-------------")
    print("    ready    ")
    print("-------------")

@client.command()
async def hello(ctx):
    await ctx.send("hello")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1318764902327914498)
    await member.send("Welcome") # Sends the user a direct message
    await channel.send(f"Welcome {member.mention}") # Sends a message in the specified channel

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1318764929066467368)
    await channel.send("Goodbye")

client.run(TOKEN)