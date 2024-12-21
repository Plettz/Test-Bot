import discord
from discord.ext import commands
from discord import app_commands
from discord import FFmpegPCMAudio

class General(commands.Cog):
        def __init__(self, client):
            self.client = client

        
        @app_commands.command(name="welcome_channel", description="Set's the channel for the welcome messages to be sent in")
        async def welcome_channel(self, interaction: discord.Interaction):
            global welcome_ID 
            welcome_ID = interaction.channel.id
            await interaction.response.send_message("Welcome messages will now be sent in this channel")


        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = self.client.get_channel(welcome_ID)
            await member.send("Welcome") # Sends the user a direct message
            if channel:
                await channel.send(f"Welcome {member.mention}") # Sends a message in the specified channel


        @app_commands.command(name="goodbye_channel", description="Set's the channel for the goodbye messages to be sent in")
        async def goodbye_channel(self, interaction: discord.Interaction):
            global goodbye_ID
            goodbye_ID = interaction.channel.id
            await interaction.response.send_message("Goodbye messages will now be sent in this channel")


        @commands.Cog.listener()
        async def on_member_remove(self, member):
            channel = self.client.get_channel(goodbye_ID)
            if channel:
                await channel.send(f"Goodbye {member}")


        @app_commands.command(name="join", description="Join's the voice channel that the user is in")
        async def join(self, interaction: discord.Interaction):
            if (interaction.user.voice):
                channel = interaction.user.voice.channel
                await channel.connect()
                await interaction.response.send_message("Joined voice channel")
            else:
                await interaction.response.send_message("You are not in a channel, please join a voice channel and try again")


        @app_commands.command(name="knock", description="Play's a knocking sound in a voice channel")
        async def knock(self, interaction: discord.Interaction):
            if (interaction.guild.voice_client):
                voice = interaction.guild.voice_client
                source = FFmpegPCMAudio("knocking-on-door.mp3")
                await interaction.response.send_message("Playing sound")
                player = voice.play(source)
            else:
                await interaction.response.send_message("Could not play sound, need to be in a voice channel")


        @app_commands.command(name="leave", description="Leave's connected voice channel")
        async def leave(self, interaction: discord.Interaction):
            if (interaction.guild.voice_client):
                await interaction.guild.voice_client.disconnect()
                await interaction.response.send_message("Disconnected from the voice channel")
            else:
                await interaction.response.send_message("I am not in a voice channel")


        @app_commands.command(name="media", description="Send's a video")
        async def media(self, interaction: discord.Interaction):
            await interaction.response.send_message(file=discord.File("Zander.mov"))


async def setup(client):
    await client.add_cog(General(client))