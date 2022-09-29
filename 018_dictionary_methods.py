my_dict = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0,
    "is_male": True
}

# make a copy
my_other_dict = my_dict.copy()

# print the copy
print(my_other_dict)

# check if the copy is equal to the original dictionary
print(my_dict == my_other_dict)  # True

# check to see if the copy IS the original dictionary
print(my_dict is my_other_dict)  # False - they occupy different spots in memory

# put last item of dictionary in a variable and remove it from the dictionary
is_male = my_dict.pop("is_male")
print(is_male)
print(my_dict)

# check if dictionaries are now equal
print(my_dict == my_other_dict)  # False

# check the length of a dictionary
print(len(my_dict))  # technically this is a function of Python and not a dictionary method but ...

popped_item = my_dict.popitem()  # pops off the last key, value pair in the dictionary
print(popped_item)

print(my_dict)

my_other_other_dict = {
    "is_male": True,
    "is_student": False
}

my_other_dict.update(**my_other_other_dict)

print(my_other_other_dict)
print(my_other_dict)
