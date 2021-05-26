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


@bot.command(name='bad')
async def bad_bot(ctx, args):
    if args == 'bot':
        angry_emoji = constants.emojis.get('angry')
        await ctx.message.add_reaction(angry_emoji)


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


bot.run(TOKEN)
