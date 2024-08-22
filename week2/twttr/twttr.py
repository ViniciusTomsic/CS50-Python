def twttr():
    twitter= input('Input: ')
    novastring=[]
    for letra in twitter:
        if letra.lower() not in ['a','e','i','o','u']:
            novastring += letra
    return novastring

final= ''.join(twttr())
print('Output: ' + final)
