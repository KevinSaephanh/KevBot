import discord

import constants


# Takes in list of words and returns a matching response from dictionary
def get_response(words: list[str]):
    command = words[1].lower()
    commands = constants.commands_tuple

    # Check if command exists in tuple
    if command not in commands:
        raise ValueError(f'{command} is not a valid command!')

    sub_command = words[2]
    if command == commands[0]:
        return constants.faces.get(sub_command)
    elif command == commands[1]:
        return constants.friends.get(sub_command)
    elif command == commands[2]:
        return constants.game.get(sub_command)


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
