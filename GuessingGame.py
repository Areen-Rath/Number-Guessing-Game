import random

number = random.randint(1, 9)
chances = 0

print("Number Guessing Game")
print("Guess a number (between 1 to 9)")

while chances <= 5:
    guess = int(input("Enter your guess: "))

    chances = chances + 1

    if guess == number:
        print("Congrats! You won the game.")
        break
    elif guess > number and chances < 5:
        print("Your guess was too high. Guess a number lesser than ", guess)
    elif guess < number and chances < 5:
        print("Your guess was too low. Guess a number higher than ", guess)
    else:
        print("You lose! The number is ", number)
