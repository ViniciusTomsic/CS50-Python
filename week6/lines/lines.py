from sys import argv, exit

if len(argv)<2:
    exit('Too few command-line arguments')
elif len(argv)>2:
    exit('Too many command-line argmuents')
else:
    file_name= argv[1]

if (file_name.split('.'))[1] != 'py':
    exit('Not a Python file')

try:
    count= 0
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip().startswith('#'):
                pass
            elif line.isspace():
                pass
            else:
                count +=1

except FileNotFoundError:
    exit('File does not exist')

print(count)
