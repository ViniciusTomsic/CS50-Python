from sys import argv,exit
import csv

def main():
    original_file,new_file= reader()
    writer(original_file, new_file)

def reader(a='csv'):
    if len(argv)<3:
        exit('Too few command-line arguments')
    elif len(argv)>3:
        exit('Too many command-line argmuents')
    elif (argv[1].split('.'))[1] != a:
        exit(f'Could not read {argv[1]}')
    else:
        return argv[1],argv[2]

def writer(o, n):
    data= []
    with open(o) as file:
            reader= csv.reader(file)
            for line in reader:
                try:
                    second = line[0].split(',')[0].strip()
                    first = line[0].split(',')[1].strip()
                    house = line[1].strip()
                    l=[{'first': first, 'last': second, 'house': house}]
                    data.append(l)
                except IndexError:
                    pass


    with open(n, 'w', newline='') as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerows(line)

if __name__ == "__main__":
    main()

