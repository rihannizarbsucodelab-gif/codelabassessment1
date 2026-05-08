## Exercise 5: Days of the Month - 30 Marks

# dictionary of months and days

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

#user input

month = int(input("Enter the month number (1-12): "))

#chack valid month

if month in days_in_month:

    #special case for February
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").lower()
        if leap_year == "yes":
            print("The number of days in February is: 29")
        else:
            print("The number of days in February is: 28")
    else:
        print(f"The number of days in month {month} is: {days_in_month[month]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")