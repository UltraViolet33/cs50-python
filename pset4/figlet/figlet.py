import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '-font'):
    if sys.argv[2] in fonts:
        font = sys.argv[2]
        figlet.setFont(font=font)
        text = input("Input: ")
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
