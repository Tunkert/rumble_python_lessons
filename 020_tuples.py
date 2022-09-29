# tuples are immutable
names = ("Tim", "Sarah", "Joe", "Aaron", "Matt")

# access a tuple from the index
# print the first item of the tuple
print(names[0])

# print the last item of the tuple
print(names[-1])

# print the length of the tuple
print(len(names))

# iterate through a tuple with a for loop
for name in names:
    if name != "Matt":
        print(name, end=", ")
    else:
        print(name)

# print an unformatted tuple
print(names)
