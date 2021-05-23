import constants

# Use constants dictionary
constants = constants.constants


def get_word_in_message(message, index):
    return message.split(' ')[index]


def is_valid_first_word(first_word):
    return first_word.lower() == '!kevbot'


def is_valid_command(message):
    # Check if first word of message == '!kevbot'
    first_word = get_word_in_message(message, 0)
    if not is_valid_first_word(first_word):
        return False

    # Check if command matches a key in constants dictionary
    command = get_word_in_message(message, 1)
    return command.lower() in constants.keys()


def get_matching_command(message):
    command = get_word_in_message(message, 1)
    return constants.get(command)
