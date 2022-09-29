# create a function that prints to the console "Hello"
def hello():
    print("hello")


print(type(hello))  # <class 'function'>
print(type(hello()))  # calls function, prints hello, and prints <class 'NoneType'>

# call the function again - note, you must call the function to have it execute
hello()


# functions with return statements
def say_hello():
    return "say hello"


# now we can set the function equal to a variable
greeting = say_hello()

# and then print it
print(greeting)


# function that has parameters
def square(num):  # the parameter is num
    return num * num


# print function square after passing in the argument 3
print(square(3))  # prints 9 to the console


# function that takes in a list
def sum_list(*args):  # the convention is to use *args but you could use *whatevs
    sum = 0
    for num in args:  # for loop will learn more later ...
        sum += num
    return sum


# call sum_list in a print function and pass Spaceballs list into, unpack list
print(sum_list(*[1, 2, 3, 4, 5]))
