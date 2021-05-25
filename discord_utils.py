import discord

import constants


def get_response(command: str, arg: str):
    commands = constants.commands_tuple

    # Check if command exists in tuple
    if command not in commands:
        raise ValueError(f'{command} is not a valid command!')

    if command == commands[0]:
        return constants.friends.get(arg)
    elif command == commands[1]:
        return constants.game.get(arg)


def get_image_response_text(filename: str):
    images = constants.images
    if filename in images:
        return images[filename]
    return


def get_image_source(filename: str):
    images = constants.image_sources
    if filename in images:
        return images[filename]
    return


def get_emoji(message, name):
    return discord.utils.get(message.guild.emojis, name=name)
