def main():
    text= input("What's up? ")
    print(convert(text))

def convert(txt):
    txt= txt.replace(":)", "🙂").replace(":(", "🙁")
    return txt

main()
