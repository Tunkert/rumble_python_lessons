# dictionaries are a very important data type in Python consisting of key, value pairs
my_dict = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0,
    "is_male": True
}

# dictionaries can be accessed via the key
print(my_dict["name"])  # prints 'Timothy Unkert' to the console
print(my_dict["age"])  # prints 46 to the console
print(my_dict["GPA"])  # prints 4.0 to the console
print(my_dict["is_male"])  # prints True to the console

# we can also iterate through the keys using a for loop
for k in my_dict.keys():
    print(k)

# additionally we can iterate through the values using a for loop
for v in my_dict.values():
    print(v)

# finally we can iterate through a dictionary's key, value pairs using a for loop
for k, v in my_dict.items():
    print(k, ":", v)
   