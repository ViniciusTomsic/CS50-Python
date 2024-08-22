from sys import argv, exit
import requests
import json

def main():
    if len(argv)!= 2:
        exit('Missing command-line argument')
    elif floater(argv)== False:
        exit('Command-line argument is not a number')
    else:
        web_list= requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        search= web_list.json()
        price= search["bpi"]["USD"]["rate_float"]
        value= floater(argv)*price
        return print(f'${value:,.4f}')



def floater(n):
    n= n[1]
    try:
        return float(n)
    except ValueError:
        return False

main()

