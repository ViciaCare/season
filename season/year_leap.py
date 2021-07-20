import calendar

year=int(input("Введите год " ))


def is_year_leap():
    result=calendar.isleap(year)
    print(result)


is_year_leap()
