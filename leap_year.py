def is_leap_year(leapyear):

    if leapyear%4==0:
        if leapyear%100==0:
            if leapyear%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    month_days=[30,28,31,30,31,30,31,30,31,30,31,30,31,30,31]
    if is_leap_year(year) and month==2:
        return 29
    return month_days[month-1]
year=int(input("enter the year"))
month=int(input("enter a month"))

days=days_in_month(year,month)
print(days)
