import random
from words import words
import string


def get_valid_word(w):  # make sure the randomly selected word doesnt have spaces or dashes
    word = random.choice(w)
    while '-' in word or ' ' in word:
        word = random.choice(w)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # list of all letters in the word
    alphabet = set(string.ascii_uppercase)  # predetermined list of letters of the english alphabet
    used_letter = set()  # list of letters that the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:  # because for every correctly guessed letter of the word, the letter
        # is removed from the list of word letters, this says that while there are still letters that have not been
        # eliminated

        print('You have', lives, 'lives left and You have used these letters: ', ' '.join(used_letter))  # ['a','b',
        # 'cd'] --> 'a b cd'

        # what current word is --> (W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]  # list of the word with the letters
        # that have been guess and dashes where the letter has not been guessed
        print(' '.join(word_list))
        print()

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:  # if a user input letter is a valid letter of the alphabet AND IS NOT
            # ALREADY IN USED_LETTER
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word')

        elif user_letter in used_letter:  # if the user has already guessed that letter
            print("You have already used that character. Please try again")
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('\nYou died, sorry. The word was', word)
    else:
        print('\nYou guessed the word', word, '!!')


print(hangman())
