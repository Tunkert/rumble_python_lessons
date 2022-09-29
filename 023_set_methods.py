names_set = set(("Tim", "Aaron", "Joe", "Sarah", "Billy", "Ben"))  # create a set from a tuple
# this gives a warning - can be replaced with set literal, like below
names_set_2 = {"Tim", "Joe", "Aaron"}

print(names_set)

# pop an item of the set and assign it to a variable, remember sets have no order
last_item = names_set.pop()
print(last_item)
print(names_set)

# add an item to the set
names_set.add("Johnny")
print(names_set)

# print the difference of the two sets
print(names_set.difference(names_set_2))

# union of the two sets
my_superset = names_set.union(names_set_2)
print(my_superset)

# intersection of the two sets
my_intersection = names_set.intersection(names_set_2)
print(my_intersection)

# non-intersection (symmetric difference) of the two sets
my_symmetric_diff = names_set.symmetric_difference(names_set_2)
print(my_symmetric_diff)

# clear the set
names_set.clear()
print(names_set)


