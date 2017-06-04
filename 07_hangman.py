import random

pics = ["""
    +---+
    |   |
        |
        |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
        |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
    |   |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
   /|   |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
===========
""", """
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
===========
""", """
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
===========
"""]

words = 'poop dump stinky'.split()


def get_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]
