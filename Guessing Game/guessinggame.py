import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between ! and {x}: '))
        if guess < random_num:
            print('Sorry guess again. Too low')
        elif guess > random_num:
            print('Sorry, guess again. Too high')
    print(f'Yay, congrats. You have guessed the number {random_num} correctly')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess1 = random.randint(low, high)
        else:
            guess1 = low
        feedback = input(f'Is {guess1} too high (H), too low (L) or correct (C)?').lower()
        if feedback == 'h':
            high = guess1-1
        if feedback == 'l':
            low = guess1 + 1
    print('Yay the computer guessed your number {guess1} correctly')


computer_guess(10)
