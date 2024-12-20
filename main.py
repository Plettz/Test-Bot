import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

file = open("key.txt", 'r')
TOKEN = file.read()
# print(TOKEN)

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("-------------------------------------")
    print(f"Logged in as {client.user}")
    print("-------------------------------------")

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

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

@client.tree.command(name="join", description="Join's the voice channel that the user is in")
async def join(interaction: discord.Interaction):
    if (interaction.user.voice):
        channel = interaction.user.voice.channel
        await channel.connect()
        await interaction.response.send_message("Joined voice channel")
    else:
        await interaction.response.send_message("You are not in a channel, please join a voice channel and try again")

@client.tree.command(name="knock", description="Play's a knocking sound in a voice channel")
async def knock(interaction: discord.Interaction):
    if (interaction.guild.voice_client):
        voice = interaction.guild.voice_client
        source = FFmpegPCMAudio("knocking-on-door.mp3")
        interaction.response.send_message("Playing sound")
        player = voice.play(source)
    else:
        await interaction.response.send_message("Could not play sound, need to be in a voice channel")

@client.tree.command(name="leave", description="Leave's connected voice channel")
async def leave(interaction: discord.Interaction):
    if (interaction.guild.voice_client):
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Disconnected from the voice channel")
    else:
        await interaction.response.send_message("I am not in a voice channel")

@client.tree.command(name="media", description="Send's a video")
async def media(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File("Zander.mov"))

client.run(TOKEN)