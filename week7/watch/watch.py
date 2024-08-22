import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link :=re.search(r"^<iframe .*src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)\".+iframe>$",s):
        src= link.group(1)
        return 'https://youtu.be/'+src
    else:
        return None


if __name__ == "__main__":
    main()
