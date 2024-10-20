import random
print("Random number guessing game")
guess = input("Guess a number: ")

if not guess.isnumeric():
    print("Guess must be a number")
else:
    guess = int(guess)
    number = random.randint(0, 10)
    
    if guess == number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong, the number was " + str(number))