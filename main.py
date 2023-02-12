import random
import time
import math
print('What do you want the highest number to be?')
time.sleep(1)
highList = list(range(1000, 2000))
high = random.choice(highList)
print(high)
print('What do you want the lowest number to be?')
time.sleep(1)
lowList = list(range(1, 100))
low = random.choice(lowList)
print(low)
print(f'To you: Please choose a number from {high} to {low}.')
while True:
    number = input()
    if not number.isnumeric():
        print('Sorry, but that symbol is invalid.')
        print('Please retype the number.')
    else:
        number = int(number)
        if number < low:
            print(f'Sorry, but the number you inputted is smaller than the smallest number limit ({low}).')
            print('Please retype the number.')
        elif number > high:
            print(f'Sorry, but the number you inputted is bigger than the highest number limit ({high}). ')
            print('Please retype the number.')
        else:
            break
print('To You: How much guesses will you allow the computer?')
while True:
    guessesLeft = input()
    if not guessesLeft.isnumeric():
        print('Sorry, but that symbol is invalid.')
        print('Please retype the number.')
    else:
        guessesLeft = int(guessesLeft)
        if guessesLeft < 5:
            print('Sorry, but the number you inputted is smaller than the smallest number limit (5).')
            print('Please retype the number.')
        elif guessesLeft > 30:
            print(f'Sorry, but the number you inputted is bigger than the highest number limit (30). ')
            print('Please retype the number.')
        else:
            break
print("\n"*20)
for i in range(guessesLeft):
    print('Computer Guessing...')
    time.sleep(1)
    possibilities = list(range(low, high))
    midpoint = low+high
    midpoint = midpoint / 2
    midpoint = math.ceil(midpoint)
    guess = midpoint
    print(guess)
    if guess > number:
        print('[Too Big]')
        high = guess
    elif guess < number:
        print('[Too Small]')
        low = guess
    elif guess == number:
        print('[The Configuration Has Guessed The Number]')
        exit()
    if i == guessesLeft-1:
        print('[The Configuration Has Not Guessed The Number]')
        exit()
