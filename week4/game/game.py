from random import randint
from sys import exit

def main():
    range= get_number()
    x= randint(1,range)
    while True:
        try:
            guess= int(input('Guess: '))
            if guess < 0:
                pass
            else:
                if guess < x:
                    print('Too small!')
                elif guess > x:
                    print('Too large!')
                else:
                    exit('Just right!')
        except ValueError:
            pass

def get_number():
    while True:
        try:
            level= int(input("Level: "))
            if level <= 0:
                pass
            else:
                return level
        except ValueError:
            pass
main()
