def parse_month(month):
    if month == 'January':
        return '01'
    elif month == 'February':
        return '02'
    elif month == 'March':
        return '03'
    elif month == 'April':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'June':
        return '06'
    elif month == 'July':
        return '07'
    elif month == 'August':
        return '08'
    elif month == 'September':
        return '09'
    elif month == 'October':
        return '10'
    elif month == 'November':
        return '11'
    elif month == 'December':
        return '12'
    else:
        print("Something went wrong.")

def parse_date(user_string):
    month = user_string[0:user_string.index(' ')]

    day = user_string[user_string.index(' ') + 1:user_string.index(',')]
    if int(day) < 10:
        day = '0' + day

    year = date[date.index(',') + 2:]

    return f'{parse_month(month)}/{day}/{year}'


if __name__ == '__main__':
    while True:
        date = input()
        if date == '-1':
            break
        print(parse_date(date))