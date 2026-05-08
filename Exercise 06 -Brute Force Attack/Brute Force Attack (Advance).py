## Exercise 6: Brute Force Attack - 30 Marks

# correct password

correct_password = "12345"

attempts = 5

#loop to ask for the password until the correct one is entered or attempts are exhausted

while attempts > 0:
    password_input = input("Enter the password: ")
    if password_input == correct_password:
        print("Access granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts left. Try again.")
        else:
            print("Incorrect password. No attempts left. Access denied.")
    
