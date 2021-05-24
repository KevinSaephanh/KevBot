import os

import discord
from dotenv import load_dotenv

import constants
from discord_utils import get_response, get_image_response_text, get_image_source

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

    # Parse words in message to list
    words = message.content.split(' ')

    # Check if message has sufficient words for a command
    # or if prefix of message is correct
    if len(words) < 2 or words[0].lower() != '!kevbot':
        return

    # Get bot response to message
    commands = constants.commands_tuple
    try:
        if set(words).intersection(set(commands)):
            if 'image' in words:
                filename = words[2]
                message_response = get_image_response_text(filename)
                image_source = get_image_source(filename)
                await message.channel.send(message_response, file=discord.File('assets/' + image_source))
            else:
                response = get_response(words)
                await message.channel.send(response)
    except Exception:
        raise discord.DiscordException


client.run(TOKEN)
