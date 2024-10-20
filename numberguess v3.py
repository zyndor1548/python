import random
print("\n" * 10)

def firsthint(number):
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

def secondhint(number, firstguess):
    difference = abs(number - firstguess)
    if difference > 10:
        near = "You should have read the first hint!"
    else:
        if number == 0:
            print("if this number is b then a - b = a")
        else:
            if difference < 3:
                near = "very near"
            elif difference <= 5:
                near = "not too far"
            else:
                near = "quite far"
            if number < firstguess:
                print(f"The number you guessed is bigger than the original number and \n{near} to the original number.")
            elif number > firstguess:
                print(f"The number you guessed is smaller than the original number and \n{near} to the original number.")
print("Random number guessing game")
number = random.randint(0, 50)
firsthint(number)
firstguess = input("Guess a number: ")
if not firstguess.isnumeric():
    print("Guess must be a number")
else:
    firstguess = int(firstguess)
    if firstguess == number:
        print("You guessed correctly!")
    else:
        print("You guessed the wrong number")
        secondhint(number, firstguess)
        secondguess = input("Guess again: ")
        
        if not secondguess.isnumeric():
            print("Guess must be a number")
        else:
            secondguess = int(secondguess)
            if secondguess == number:
                print("You guessed correctly!")
            else:
                print(f"You guessed wrong again. The correct number was {number}.")
