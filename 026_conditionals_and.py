# conditionals with user input and the and keyword
age = int(input("Enter your age: "))
if age >= 21:
    has_id = input("Do you have your id? (y/n) ")
else:
    has_id = "y"

if age >= 21 and has_id == "y":
    print("You can enter the bar!")
elif age >= 18 and has_id != "n":
    print("You can go to war but you can't enter the bar.")
elif age >= 18 and has_id == "n":
    print("Sorry, I need an ID.")
else:
    print("You're a minor.")