# different data types - in this file I'll cover the fundamentals
name = "Timothy Unkert"

# find the type of name
print(type(name))  # <class 'str'>

# create a variable (container) to hold a number
num1 = 3

# find the type of num1
print(type(num1))  # <class 'int'>

# create another container to hold a number with a decimal
num2 = 3.14

# find the type
print(type(num2))  # <class 'float'>

# complex numbers ...
comp1 = 4 + 2j

# find the type of comp1
print(type(comp1))

# create a true / false variable
my_bool = True

# find the type of my_bool
print(type(my_bool))  # <class 'bool'> - this is a boolean

# create a list
my_list = [1, 2, 3, 4, 5]  # this is referred to as an array in many other languages

# find the type of my_list
print(type(my_list))  # <class 'list'>

# create a tuple - immutable iterable
my_tup = (1, 2, 3, 4, 5)

# print the type
print(type(my_tup))  # <class 'tuple'>

# create a set
my_set = {1, 2, 3, 4, 5}

# print the type
print(type(my_set))  # <class 'set'>

# create a dictionary
my_dict = {
    "name": "Timothy",
    "age": 46,
    "GPA": 4.0,
    "is_male": True
}

# print the type
print(type(my_dict))  # <class 'dict'>


def my_func():
    print("This is my func!")


# print the type
print(type(my_func()))  # <class 'NoneType'>
