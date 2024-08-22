menu= {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    acount=0.00
    while True:
        try:
            order= input('Item: ').lower()
            if order in menu:
                acount += (menu[order])
                print(f'Total: ${acount:.2f}')
            else:
                pass
        except EOFError:
            return

main()
