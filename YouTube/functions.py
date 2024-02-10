from datetime import datetime, date, time, timedelta

# current_date_time = datetime.now()
# current_date = current_date_time.date()
# print((current_date - date(2022, 1, 1)).days)

def week(no):
    if no<14:
        return 1
    elif no>=14 or no<21:
        return 2
    else:
        return 3
    
def month(no):
    if no<56:
        return 1
    elif no>=56 or no<84:
        return 2
    elif no>=84 or no<112:
        return 3
    elif no>=112 or no<140:
        return 4
    elif no>=140 or no<168:
        return 5
    elif no>=168 or no<196:
        return 6
    elif no>=196 or no<224:
        return 7
    elif no>=224 or no<252:
        return 8
    elif no>=252 or no<280:
        return 9
    elif no>=280 or no<308:
        return 10
    elif no>=308 or no<336:
        return 11
    else:
        return 12

def convert(no):
    if no<7:
        return f'Uploaded {no} days ago'
    elif no>=7 or no<28:
        return f'Uploaded {week(no)} weeks ago'
    elif no>=28:
        return f'Uploaded {month(no)} months ago'
    elif no>=336:
        return f'Uploaded {int(no/336)} years ago'
