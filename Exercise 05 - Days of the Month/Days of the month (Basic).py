#Exercise 5: Days of the Month - 30 Marks

#dictionary of months and Days

# dictionary of months and days

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
    }

#ask the user for the month number

month = int(input("Enter the month number (1-12): "))

#check and output

if month in days_in_month:
    print(f"The number of days in month {month} is: {days_in_month[month]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")