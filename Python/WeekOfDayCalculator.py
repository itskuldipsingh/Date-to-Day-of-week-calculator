while True:
    while True:
        year = int(input("Enter year or ctrl+c to exit: "))
        if 0 <= year <= 9999:
            break
        else:
            print("Invalid year. Please enter a correct year between 0 and 9999.")

    leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    while True:
        month = int(input("Enter month or ctrl+c to exit: "))
        if 1 <= month <= 12:
            break
        else:
            print("Invalid month. Please enter a correct month.")

    while True:
        date = int(input("Enter date or ctrl+c to exit: "))
        if (
            (leap_year and month == 2 and 0 <= date <= 29)
            or (not leap_year and month == 2 and 0 <= date <= 28)
            or (month in [1, 3, 5, 7, 8, 10, 12] and 0 <= date <= 31)
            or (month in [4, 6, 9, 11] and 0 <= date <= 30)
        ):
            break
        else:
            print("Invalid date. Please enter a correct date.")

    century = (year // 100) * 100

    if century % 400 == 0:
        century_code = 6
    elif century % 400 == 100:
        century_code = 4
    elif century % 400 == 200:
        century_code = 2
    elif century % 400 == 300:
        century_code = 0

    last_2digit_of_year = year % 100

    if leap_year:
        month_codes = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
    else:
        month_codes = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

    month_code = month_codes[month - 1]

    day_of_week = (last_2digit_of_year + last_2digit_of_year // 4 + date + month_code + century_code) % 7

    if day_of_week == 1:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Sunday.")
    elif day_of_week == 2:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Monday.")
    elif day_of_week == 3:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Tuesday.")
    elif day_of_week == 4:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Wednesday.")
    elif day_of_week == 5:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Thursday.")
    elif day_of_week == 6:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Friday.")
    elif day_of_week == 0:
        print(f"The day of the week for {year}-{month:02d}-{date:02d} is Saturday.")
