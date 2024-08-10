import random
level = "pp"
guess = "pp"


while not level.isdigit():
    level = input("Level: ")

answer = random.randint(0, int(level))



while True:
    if not guess.isdigit():
        guess = input("Guess: ")

    elif int(guess) < 1:
        guess = input("Guess: ")

    elif int(guess) > answer:
        print("Too large!")
        guess = input("Guess: ")

    elif int(guess) < answer:
        print("Too small!")
        guess = input("Guess: ")

    else:
        print("Just right!")
        break

