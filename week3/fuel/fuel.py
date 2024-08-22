def main():
    while True:
        fraction= input('Fraction: ')
        if integer(fraction)==False:
            pass
        else:
            y,z= integer(fraction)
            try:
                x= round(round((y/z),2)*100)
                if x>100:
                    pass
                elif 98< x <=100:
                    return print('F')
                elif x<2:
                    return print('E')
                else:
                    return print(f'{x}%')

            except ZeroDivisionError:
                pass

def integer(x):
    numbers= x.split('/')
    try:
        y= int(numbers[0])
        z= int(numbers[1])
        return y, z
    except ValueError:
        return False


main()
