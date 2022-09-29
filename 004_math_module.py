# you can import modules in Python to get more functionality
import math

# take the square root of a number
print(math.sqrt(10))

# take the integer square root of a number
print(math.isqrt(10))

# trig functions - they take in radians
print(math.sin(math.pi / 4))  # you can also do cosine, tangent, arcsine, etc.

# find the hypotenuse of a right triange
print(math.hypot(3, 4))  # 5.0

# raise a number to a power, different method
print(math.pow(2, 3))  # 8.0

# take a logarithm
print(math.log(8, 2))  # log 8 with base 2 is 3 because 2^3 = 8

# round up to the next integer
print(math.ceil(3.1))  # 4

# round down to the lower integer
print(math.floor(3.1))

# raise e to a power
print(math.exp(5))  # e^5

# convert degrees to radians
print(math.radians(45))  # pi / 4

# find the factorial of 5
print(math.factorial(5))  # 120

# find the absolute value of a number
print(math.fabs(-10))
