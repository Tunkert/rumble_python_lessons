# take in user input and assign it to a variable
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

sum = num1 + num2

print("The sum is {}.".format(sum))  # this will give you 34 which is not right - it's 'adding' strings

# use type conversion
num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))

sum2 = num3 + num4

print(f"The sum is {sum2}.")  # this yields 7, the correct result.
