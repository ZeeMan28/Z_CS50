
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()
figlet_list = figlet.getFonts()



if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet_list:

    text = input("Input: ")

    figlet.setFont(font=sys.argv[2])

    print(figlet.renderText(text))


elif len(sys.argv) == 1:
    
    text = input("Input: ")

    figlet.setFont(font = figlet_list[random.randint(0, len(figlet_list))])

    print(figlet.renderText(text))

else:
    sys.exit("Invalid usage")

