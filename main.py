import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os

file = open("key.txt", 'r')
TOKEN = file.read()
# print(TOKEN)

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("-------------------------------------")
    print(f"Logged in as {client.user}")
    print("-------------------------------------")

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load {filename}: {e}')

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} slash commands successfully!")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

    print(f"Bot is connected to {len(client.guilds)} guild(s).")


@client.command()
async def hello(ctx):
    await ctx.send("hello")

client.run(TOKEN)