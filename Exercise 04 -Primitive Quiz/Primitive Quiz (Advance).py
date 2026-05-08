## Exercise 4: Primitive Quiz - 30 Marks

#dictionary to questions and answers

quiz = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "India": "New Delhi",
    "Brazil": "Brasilia",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Canada": "Ottawa",
    "Russia": "Moscow",
    "China": "Beijing",
    "Sweden": "Stockholm"
}

#loop through the quiz 

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Wrong answer. The correct answer is {capital}.")