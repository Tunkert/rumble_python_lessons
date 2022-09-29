names = ("Tim", "Sarah", "Aaron", "Joe", "Matt", "Ben", "Joe")

# find the index of an item in the tuple
print(names.index("Sarah"))

# find the count of a certain item in the tuple
print(names.count("Joe"))

print(names.__add__(("Joe", "Sam", "Rick")))  # this does not persist but concatenates two tuples together
print(names)
