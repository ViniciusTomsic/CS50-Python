def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)> 6 or len(s)< 2:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    elif is_pontuation(s)== True:
        return False
    elif zero_first(s)== True:
        return False
    elif number_midle(s)== True:
        return False
    else:
        return True

def is_pontuation(p):
    ponto= 0
    for character in p:
        if character in ['.','>',',','<','[','?']:
            ponto += 1
    if ponto > 0:
        return True
    else:
        return False

def zero_first(w):
    for character in w:
        if character.isdigit() == True:
            if character == '0':
                return True
            else:
                return False
    return False

def number_midle(z):
    i=0
    while i < len(z)-1:
        if z[i].isdigit() == True:
            i+=1
            if z[i].isalpha()==True:
                return True
        else:
            i += 1
    return False

main()
