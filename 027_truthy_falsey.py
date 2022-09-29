num1 = int(input("Enter an integer: "))

if num1:
    print("You entered an integer other than 0.")
else:
    print("You entered 0.")

# this works because 0 is falsey and any number other than 0 is truthy
