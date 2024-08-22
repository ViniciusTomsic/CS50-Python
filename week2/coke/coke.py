def main():
    price= 50
    amount= 0
    print("Amount Due: " + str(price))
    while amount < price:
        coin= int(input('Insert Coin: '))
        if coin==25 or coin== 10 or coin==5:
            amount += coin
            if amount < price:
                print('Amount Due: ' + str(price-amount))
            else:
                change= amount - price
                print('Change Owed: '+str(change))
        else:
            print('Amount Due: ' + str(price-amount))


main()
