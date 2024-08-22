from tabulate import tabulate
from sys import argv, exit
from csv import DictReader

def main():
    file = reader()
    menu= dict_creator(file)
    print(tabulate(menu,headers='keys',tablefmt='grid'))

def reader():
    if len(argv)<2:
        exit('Too few command-line arguments')
    elif len(argv)>2:
        exit('Too many command-line argmuents')
    elif (argv[1].split('.'))[1] != 'csv':
        exit('Not a Python file')
    else:
        return argv[1]


def dict_creator(file):
    with open(file, 'r') as csv_file:
        csv_reader= DictReader(csv_file)
        dictionarie= []

        for line in csv_reader:
            dictionarie.append(line)
    return dictionarie


main()
