greetings= input("Greeting: ").lower().replace(',',' ').strip()

words= greetings.split()

first_word= words[0]


first_letter= first_word[0]


if first_word== "hello":
    print('$0')
elif first_letter== 'h':
    print('$20')
else:
    print('$100')


