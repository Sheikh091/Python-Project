print("Hello World")
print("Salam My Name is Musa")

import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the nunber between 1 and 100: "))

    if guess == secret_number:
        print("Congratulations! You guess the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too High! Try again")