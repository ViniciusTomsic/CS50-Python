expression= input('Expression: ').split()


x= int(expression[0])
y= int(expression[2])



def inter(l):
    x= int(l[0])
    y= int(l[2])
    if l[1]== '+':
        return print(float(x + y))
    elif l[1]== '*':
        return print(float(x*y))
    elif l[1]== '-':
        return print(float(x-y))
    else:
        return print(float(x/y))

inter(expression)
