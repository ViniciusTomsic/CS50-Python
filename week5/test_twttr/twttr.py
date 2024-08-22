def main():
    twitter= input('Input: ')
    return shorten(twitter)

def shorten(a):
    novastring=[]
    for letra in a:
        if letra.lower() not in ['a','e','i','o','u']:
            novastring += letra
    return ''.join(novastring)

if __name__ == "__main__":
    main()
