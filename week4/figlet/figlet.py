from pyfiglet import Figlet
from sys import argv, exit
from random import choice

figlet= Figlet()

def main():
    if len(argv)==1:
        user_input= input('Input: ')
        font_random= choice(figlet.getFonts())
        figlet.setFont(font=font_random)
        return print(figlet.renderText(user_input))

    elif len(argv)==3:
        if argv[1]== '-f' or argv[1]== '--font':
            user_font= argv[2]
            if user_font not in figlet.getFonts():
                exit('Invalid uasge')
            else:
                user_input= input('Input: ')
                figlet.setFont(font=user_font)
                return print(figlet.renderText(user_input))
        else:
            exit('Invalid usage')

    else:
        exit('Invalid usage')
main()
