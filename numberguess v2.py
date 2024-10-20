import random
print("Random number guessing game")
number = random.randint(0, 50)
if number <= 10:
    print("Hint: number is under 10")
elif number <= 20:
    print("Hint: number is between 10 and 20")
elif number <= 30:
    print("Hint: number is between 20 and 30")
elif number <= 40:
    print("Hint: number is between 30 and 40")
else:
    print("Hint: number is between 40 and 50")

guess = input("Guess a number: ")

if not guess.isnumeric():
    print("Guess must be a number")
else:
    guess = int(guess)
    if guess == number:
        print("You guessed correctly!")
    else:
        print("You guessed wrong, the number was " + str(number))