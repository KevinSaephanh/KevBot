import os

import discord
from dotenv import load_dotenv

import validator
import constants

# Get env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user} is connected to: {guild.name}\n')


@client.event
async def on_message(message):
    # Check if message was sent from bot
    if message.author == client.user:
        return

    # Validate message format
    content = message.content
    if validator.is_valid_command(content):
        response = validator.get_matching_command(content)
        await message.channel.send(response)
    else:
        return


client.run(TOKEN)
