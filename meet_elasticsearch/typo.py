from random import randint, choice
from string import ascii_letters


def raw(name):
    """Get the unmodified name.

    :return: 
    """
    return name


def _levenshtein(name, distance=1):
    """Apply a Levenshtein-Damerau transformation to the name.

    :param distance: The desired edit distance (default=1)
    :return: The modified name
    """
    word = random_word(name)

    return name.replace(
        word,
        _levenshtein_word(name, distance=distance, word=word)
    )


def _levenshtein_word(name, distance=1, word=None):
    """Apply a Levenshtein-Damerau transformation to a word in the name.

    :param distance: 
    :param word: 
    :return: 
    """
    if word is None:
        word = random_word(name)

    chars = list(word)

    for i in range(0, distance):
        int = randint(0, 2)

        if int == 0:  # Add a character
            chars.insert(randint(0, len(chars)), choice(ascii_letters[:26]))
        elif int == 1:  # Remove a character
            del (chars[randint(0, len(chars) - 1)])
        else:  # Swap two characters
            position = randint(0, len(chars) - 1)
            char = chars[position]
            del (chars[position])
            chars.insert(position + 1, char)

    return ''.join(chars)


def remove_space(name):
    """Remove a random space from the name.

    :return: The modified name
    """
    chars = list(name)
    spaces = [i for i, char in enumerate(chars) if char == ' ']

    if len(spaces) > 1:
        del (chars[choice(spaces)])

    return ''.join(chars)


def add_space(name):
    """Add a random space to the name.

    :return: The modified name
    """
    word = random_word(name)

    return name.replace(word, add_space_word(name, word=word))


def add_space_word(name, word=None):
    """Return a word from the name, separated by a space.

    :param word: 
    :return: 
    """
    if word is None:
        word = random_word(name)

    chars = list(word)
    chars.insert(randint(1, len(chars) - 1), ' ')

    return ''.join(chars)


def levenshtein_1(name):
    """Return the name where one of the words contains a LD transformation.

    :return: 
    """
    return _levenshtein(name, 1)


def levenshtein_2(name):
    """Return the name where one of the words contains 2 LD transformations.

    :return: 
    """
    return _levenshtein(name, 2)


def levenshtein_word_1(name):
    """Return a word from the name which contains a LD transformation.

    :return: 
    """
    return _levenshtein_word(name, 1)


def levenshtein_word_2(name):
    """Return a word from the name which contains 2 LD transformations.

    :return: 
    """
    return _levenshtein_word(name, 2)


def random_word(name):
    """Return a random word from the name.

    :return:
    """
    return choice(name.split())


def random_word_part(name):
    """Return a part of a random word from the name.

    :return:
    """
    word = random_word(name)

    if len(word) <= 3:
        return word

    return word[:randint(3, len(word) - 1)]
