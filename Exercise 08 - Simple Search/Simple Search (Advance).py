## Exercise 8: Simple Search - 30 Marks

#list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#user input for name to search
search_name = input("Enter the name to search: ")

#search for the name
if search_name in names:
    print(f"{search_name} is in the list.")
else:
    print(f"{search_name} is not in the list.")