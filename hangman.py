import os
import sys
import random

#f = open('./words.txt', 'r')
#word_list = [line.split(', ') for line in f.readlines()]
#words = random.choice(word_list)

f = open('./wiki-1k.txt', 'r')
word_list = f.readlines()


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    for letter in secret_word[:-1]:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
    print('')

def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(word_list)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses, good_guesses)

        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                print("You win! The word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("You lost! The word was {}".format(secret_word))
                done = True

        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play (done = False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter to start, Q to quit")
    if start.lower() == 'q':
        sys.exit()

print('Welcome to Hangman!')

done = False

while True:
    clear()
    welcome()
    play(done)
