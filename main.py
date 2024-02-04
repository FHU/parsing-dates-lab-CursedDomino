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
        print('Something went wrong.')


date = input()

def parse_date(user_string):
    month = date[0:date.index(' ')]

    day = date[date.index(' ') + 1:date.index(',')]
    if int(day) < 10:
        day = '0' + day

    year = date[date.index(',') + 2:]

    return f'{parse_month(month)}/{day}/{year}'


if __name__ == '__main__':
    print(parse_date(date))