import random
random_number = random.randint(0,100)

print("This is the game of higher or lower \nThe aim of the game is to guess a number between 0 and 100 in the least amount of guesses as possible \n")

def higher_or_lower(guess, count):
    if guess < random_number:
        print("The number is higher")
    elif guess > random_number:
        print("The number is lower")
    elif guess == random_number:
        if count == 1:
           print("Correct! You completed the game in", count, "guess") 
        else:  
           print("Correct! You completed the game in", count, "guesses")
        return True
    return False

def user_guess():
    guess = ''
    count = 0
    set_of_guesses = set()
    while True:
        guess = input('Guess a number: ')
        if guess.isdigit() == True:
           guess = int(guess)
           if guess not in set_of_guesses:
              set_of_guesses.add(guess)
              count = count + 1
           guessed_correctly = higher_or_lower(guess, count)
           if guessed_correctly:
               break
        else:
           print('Not a valid guess')
        
guess = user_guess()