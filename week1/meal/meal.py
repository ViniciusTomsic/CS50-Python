def main():
    hour= input("What time is it? ")
    time= convert(hour)
    if 7 <= time <= 8:
        return print('breakfast time')
    elif 12 <= time <= 13:
        return print('lunch time')
    elif 18 <= time <= 19:
        return print('dinner time')



def convert(time):
    time= time.split(':')
    hora= round(float(time[0]),1)
    min= round(float(time[1]),1)
    percent= min/60;
    time= hora+percent;
    return time


if __name__ == "__main__":
    main()
