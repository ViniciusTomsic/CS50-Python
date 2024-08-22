months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date= input('Date: ')
        try:
            date= convert_date(date)
            if date_checker(date):
                return print(f'{date[2]}-{date[0]}-{date[1]}')

            else:
                pass
        except ValueError:
            pass

def convert_date(d):
    date_formated=[]
    if len(d.split('/'))==3:
        d=d.replace(' ','')
        date_split= d.split('/')
        for argumento in date_split:
            if int(argumento) <10:
                date_formated.append(argumento.zfill(2))
            else:
                date_formated.append(argumento)

    else:
    
        d = d.replace(',','')
        date_split= d.split()
        month= months.index(date_split[0])+1
        date_split[0]=str(month)

        for argumento in date_split:
            if int(argumento) <10:
                date_formated.append(argumento.zfill(2))
            else:
                date_formated.append(argumento)


    return date_formated

def date_checker(d):
    day= int(d[1])
    month= int(d[0])
    if day > 31 or month > 12:
        return False
    else:
        return True

main()
