from datetime import datetime
from datetime import date
from datetime import timedelta
import sys
import inflect




def main():
    birth= input('Date of Birth: ')
    return print(converter(birth))

def converter(d,today=None):
    if not today:
        today= date.today()
    else:
        today= datetime.strptime(today, "%Y-%m-%d").date()
    p = inflect.engine()
    try:
        birth= datetime.strptime(d, "%Y-%m-%d").date()
        dif= today - birth
        minutes= int(dif.total_seconds()/60)
        string_minutes= p.number_to_words(minutes, wantlist=True, andword='')
        string= f"{string_minutes[0].capitalize()}, "

        for _ in string_minutes[1:-1]:
            string += _ + ', '
        string = string + f'{string_minutes[-1]} minutes'
        return string
    except ValueError:
        sys.exit('Invalid date')






if __name__ == "__main__":
    main()
