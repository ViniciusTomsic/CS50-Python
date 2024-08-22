from emoji import emojize

def main():
    user_input= input('Input: ')
    print('Output:' + emojize(user_input, language='alias'))

main()
