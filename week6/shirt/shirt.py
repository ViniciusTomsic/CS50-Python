from sys import argv, exit, path
from PIL import Image, ImageOps

def main():
    reader()
    with Image.open('shirt.png') as shirt:
        with Image.open(argv[1]) as im:
            size= shirt.size
            im= ImageOps.fit(im,size)
            im.paste(shirt,mask=shirt)
            im.save(argv[2])

def reader():
    if len(argv)<3:
        exit('Too few command-line arguments')
    elif len(argv)>3:
        exit('Too many command-line argmuents')
    elif (argv[1].split('.'))[1] not in ['png','jpg','jpeg']:
        exit(f'Could not read {argv[1]}')
    else:
        return argv[1],argv[2]

main()
