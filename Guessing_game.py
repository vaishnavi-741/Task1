#Task 2: Number Guessing Game 
#1. Generates a random number between 1 and 50. 
#2. Asks the user to guess the number. 
#3. Gives hints like "Too High" or "Too Low" until the user guesses correctly. 
#4. Displays how many attempts it took to guess the number.

import random
num = random.randint(1,51)
attempt = 0
while True:
    guess = int(input("Guess The Number : "))
    attempt = attempt + 1
    if guess < num:
        print("The number is greater than your guess")
    elif guess > num:
        print("The number is less than your guess")
    elif guess == num:
        print(f"Congrats! you guess the number correctly in  {attempt} attempts")
    else:
        print("invalid input")