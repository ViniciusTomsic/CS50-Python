def main():
    grocery_list= inputs()
    grocery_list= sorted(grocery_list)
    grocery_dict= dictionary(grocery_list)
    grocery_dict= contador(grocery_list,grocery_dict)
    for item in grocery_dict:
        print(f'{grocery_dict[item]} {item}')

def inputs():
    list=[]
    while True:
        try:
            entrada= input().upper()
            list.append(entrada)
        except EOFError:
            break
    return list

def dictionary(p):
    d = {}
    for item in p:
        if item not in d:
            d[item]=''
    return d

def contador(l,d):
    for item in d:
        i=0
        reps= 0
        while i < len(l):
            if l[i]==item:
                reps += 1
            i += 1
        d[item]=reps
    return d

main()
