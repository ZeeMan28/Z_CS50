import random
import time

from pyfiglet import Figlet
figlet = Figlet()

def main():
    # weewo()
    game()

def game():

    guess = int(input("guess a number"))

    number = random.randint(1, 10)
    if (guess == number):
        figlet.setFont("Banner")
        print(figlet.renderText("right!"))



def weewo():
    for i in range(0, 15, 2):
        for j in range(i):
            print(".", end="")
        time.sleep(.1)
        print("")

    for i in range(16, 0, -2):
        for j in range(i):
            print(".", end="")
        time.sleep(.1)
        print("")




if __name__ == "__main__":
    main()
