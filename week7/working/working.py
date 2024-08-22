import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if re.search(r"^.+:.+ .+ to .+:.+ .+$",s):
        if hour := re.search(r"^([1][0-2]|[0-9]):([0-5][0-9]) (AM|PM) to ([1][0-2]|[0-9]):([0-5][0-9]) (AM|PM)$",s):
            in_hour, in_minute, in_period, out_hour, out_minute, out_period= hour.groups()
            if in_period == 'PM' and in_hour !='12':
                in_hour= int(in_hour)+12
            if out_period == 'PM' and out_hour !='12':
                out_hour= int(out_hour)+12
            if in_hour == '12' and in_period== 'AM':
                in_hour= 0
            if out_hour == '12' and out_period== 'AM':
                out_hour= 0
            return f"{int(in_hour):02}:{in_minute} to {int(out_hour):02}:{out_minute}"
        else:
            raise ValueError
    else:
        if hour := re.search(r"^([1][0-2]|[0-9]) (AM|PM) to ([1][0-2]|[0-9]) (AM|PM)$",s):
            in_hour, in_period, out_hour, out_period= hour.groups()
            if in_period == 'PM' and in_hour !='12':
                in_hour= int(in_hour)+12
            if out_period == 'PM' and out_hour !='12':
                out_hour= int(out_hour)+12
            if in_hour == '12' and in_period== 'AM':
                in_hour= 0
            if out_hour == '12' and out_period== 'AM':
                out_hour= 0
            return f"{int(in_hour):02}:00 to {int(out_hour):02}:00"
        else:
            raise ValueError



if __name__ == "__main__":
    main()
