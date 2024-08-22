def main():
    names= lister()
    print()
    if len(names) == 2:
        print(f'Adieu, adieu, to {names[0]} and {names[1]}')
    elif len(names) > 2:
        print(f'Adieu, adieu, to {names[0]}', end='')
        for name in names[1:-1]:
            print(f', {name}',end='')
        return print(f', and {names[-1]}')
    else:
        print(f'Adieu, adieu, to {names[0]}')


def lister():
    lista= []
    while True:
        try:
            lista.append(input('Name: '))
        except EOFError:
            return lista

main()
