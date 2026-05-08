## Exercise 6: Brute Force Attack - 30 Marks

# correct password

correct_password = "12345"

#keep asking for the password until the correct one is entered

while True:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")