import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import constants
from discord_utils import get_response, get_image_response_text, get_image_source

# Get env variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix=constants.COMMAND_PREFIX)


@bot.command()
async def friend(ctx, arg):
    response = get_response('friend', arg)
    await ctx.channel.send(response)


@bot.command()
async def game(ctx, arg):
    response = get_response('game', arg)
    await ctx.channel.send(response)


@bot.command()
async def image(ctx, arg):
    message_response = get_image_response_text(arg)
    image_source = get_image_source(arg)
    await ctx.channel.send(
        message_response,
        file=discord.File(constants.ASSETS_PATH + image_source)
    )


@bot.event
async def on_message(message):
    content = message.content
    channel = message.channel
    last_message = await channel.fetch_message(message.channel.last_message_id)
    author = last_message.author.name

    if content in constants.trigger_messages and author != constants.KEVBOT:
        await get_emoji_reaction(message)
    await bot.process_commands(message)


async def get_emoji_reaction(message):
    content = message.content
    emojis = constants.emojis
    trigger_messages = constants.trigger_messages

    if content == trigger_messages.get('bad bot'):
        angry_emoji = emojis.get('angry')
        await message.add_reaction(angry_emoji)
    elif content == trigger_messages.get('good bot'):
        smile_emoji = emojis.get('smile')
        await message.add_reaction(smile_emoji)


bot.run(TOKEN)
