my_name = "Timothy Unkert"

print(my_name.count("t"))  # 2
print(my_name.count("i"))  # 1
print(my_name.count(" "))  # 1

print(my_name.lower())  # prints 'timothy unkert'
print(my_name.upper())  # prints 'TIMOTHY UNKERT'

my_name = "timothy unkert"

print(my_name.capitalize())  # prints 'Timothy Unkert'

print(my_name.isupper())  # False
print(my_name.upper().isupper())  # True - also check out the chaining of methods, pretty bad ass

print(my_name.isalpha())  # False
print(my_name.isascii())  # True

print(my_name.isspace())  # False

# you can access many different methods with the dot
