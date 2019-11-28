# How many days until your birthday?

import datetime

def print_header():
    print('-------------------------------')
    print('            BIRTHDAY APP')
    print('-------------------------------')

def get_birthday():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    current_yr = datetime.date(target_date.year, original_date.month, original_date.day)

    dt = current_yr - target_date
    return dt.days


def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days'.format(days))
    else:
        print('Happy Birthday!!!')

def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)

main()
