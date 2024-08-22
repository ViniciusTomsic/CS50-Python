def main():
    fraction= input('Fraction: ')
    z= convert(fraction)
    return gauge(z)


def convert(x):
    numbers= x.split('/')
    try:
        x= int(numbers[0])
        y= int(numbers[1])
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        z= x/y
        z= round(round(z,2)*100)
        return z
    except ValueError:
        raise ValueError

def gauge(z):
    if z > 98:
        return 'F'
    elif z < 2:
        return 'E'
    else:
        return f'{z}%'

if __name__ == "__main__":
    main()

gauge(50)
