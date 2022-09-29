my_name = "Timothy Unkert"
my_age = 46

# string concatenation
print("Hi, my name is " + my_name + ".")
print("Hi, my age is " + str(my_age) + ".")  # when concatenating we need to use type conversion

# string interpolation >= 3.6
print(f"Hi, my name is {my_name}.")
print(f"Hi, my age is {my_age}.")  # don't need to use type conversion

# format < 3.6
print("Hi, my name is {}.".format(my_name))
print("Hi, my age is {}.".format(my_age))  # don't need to use type conversion

# 3 different ways to get the same thing!
