def main():
    #Recebe o input, converte em lista e printa com lower case
    camel= list((input("camelCase: ")))
    list_snake= snake(camel)
    str_snake= stringer(list_snake)
    print(str_snake.lower())

def snake(w):
    #Roda a lista procurando maiúsculas e adiciona o _
    p=w.copy()
    i=0
    while i < (len(w)):
        if w[i].isupper():
            p.insert(i,'_')
            w= p.copy()
            i+=1
        i+=1
    return p

def stringer(list):
    #Transforma a lista em uma str denovo
    str= ''.join(list)
    return str

main()
