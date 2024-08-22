from random import randint


def main():
    level= get_level()
    score=0
    for i in list(range(10)):
        j=0
        x,y= generate_integer(level)
        z= x + y
        while j<3:
            try:
                print(f'{x} + {y} = ',end='')
                guess= int(input())
                if guess != z:
                    print('EEE')
                    j += 1
                    if j==3:
                        print(f'{x} + {y} = {z}')
                        break
                else:
                    if j == 0:
                        score += 1
                        break
                    else:
                        break
            except ValueError:
                j += 1
                if j==3:
                        print(f'{x} + {y} = {z}')
                        break
                pass
    return print(f'Score: {score}')



def get_level():
     while True:
        try:
            level= int(input("Level: "))
            if level <= 0 or level>3:
                pass
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level==1:
        x= randint(0,9)
        y= randint(0,9)
        return x,y

    elif level==2:
        x= randint(10,99)
        y= randint(10,99)
        return x,y

    else:
        x= randint(100,999)
        y= randint(100,999)
        return x,y

if __name__ == "__main__":
    main()
