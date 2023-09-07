import random

def check_guess(guess, number_of_guesses, random_number):
    if guess < random_number:
        print("The number is higher")
    elif guess > random_number:
        print("The number is lower")
    elif guess == random_number:
        if number_of_guesses == 1:
            print("Correct! You completed the game in",
                  number_of_guesses, "guess")
        else:
            print("Correct! You completed the game in",
                  number_of_guesses, "guesses")
        return True
    return False


def get_user_guess():
    while True:
        guess = input('Guess a number: ')
        if guess.isdigit():
            guess = int(guess)
            return guess
        else:
            print('Not a valid guess')


def number_guessing_game():
    print("This is the game of higher or lower \nThe aim of the game is to guess a number between 0 and 100 in the least amount of guesses as possible")
    random_number = random.randint(0, 100)
    set_of_guesses = set()
    while True:
        guess = get_user_guess()
        if guess not in set_of_guesses:
            set_of_guesses.add(guess)
        guessed_correctly = check_guess(
            guess, len(set_of_guesses), random_number)
        if guessed_correctly:
            break


number_guessing_game()
