def main():
    greetings= input("Greeting: ").lower().replace(',',' ').strip()
    earned= value(greetings)
    return print(f'${earned}')

def value(s):
    s= s.lower().replace(',',' ').strip()
    words= s.split()
    first_word= words[0]
    first_letter= first_word[0]

    if first_word== "hello":
        return 0
    elif first_letter== 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
