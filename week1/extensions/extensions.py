name= input("File name: ").replace('.',' ').lower().split()

def leitor(p):
    if p == 'jpg' or p == 'jpeg':
        print('image/jpeg')
    elif p == 'png':
        print('image/png')
    elif p == 'pdf':
        print('application/pdf')
    elif p == 'gif':
        print('image/gif')
    elif p == 'txt':
        print('text/plain')
    elif p == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')

if len(name)==2:
    leitor(name[1])
elif len(name)==3:
    leitor(name[2])
else:
    print('application/octet-stream')





