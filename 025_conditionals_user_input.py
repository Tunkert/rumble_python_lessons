# conditionals with user input
name = input("What is your name?\n")

if name == "Tim":
    print("You are the teacher!")
elif name == "Sarah" or name == "Sean":
    print("You are a student!")
elif name == "Ben":
    print("How many beers did you have before you wrote this code?")
else:
    print("I don't know you.")
