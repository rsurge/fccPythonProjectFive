import random
from wordlist import words


def valid_answer(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input('Guess a letter: ').upper()


user_input = input('Type something: ')
print(user_input)
