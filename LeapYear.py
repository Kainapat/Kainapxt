def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return year + (400 - (year % 400))
    else:
        if year % 4 == 0:
            return True
        else:
            return year + (4 - (year % 4))

year = int(input("Enter a year: "))
if is_leap_year(year) == True:
    print(f"{year} is a leap year.")
else:
    print(f"The next leap year is {is_leap_year(year)}.")
