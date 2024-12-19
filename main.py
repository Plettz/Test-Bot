import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

file = open("key.txt", 'r')
TOKEN = file.read()
# print(TOKEN)

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

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a channel, please join a voice channel and try again")

@client.command()
async def knock(ctx):
    if (ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio("knocking-on-door.mp3")
        player = voice.play(source)
    else:
        await ctx.send("Could not play sound, need to be in a voice channel")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel")

client.run(TOKEN)