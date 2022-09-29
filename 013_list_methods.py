my_nums = [1, 2, 3, 4, 5]

print(my_nums.count(1))

# add an item to the list (you can append one item at a time)
my_nums.append(1)

print(my_nums.count(1))
print(my_nums)

# extending a list - add multiple items to a list
my_nums.extend([6, 7, 8, 9, 10])
print(my_nums)

# remove the last item of the list and store it to a variable
last_list_item = my_nums.pop()
print(last_list_item)
print(my_nums)

my_new_list = my_nums.copy()
print(my_new_list)

print(my_nums == my_new_list)  # True
print(my_nums is my_new_list)  # Even though they are equal this is false because they occupy separate spots in memory

my_new_list.clear()  # clear the list
print(my_new_list)

# find the index of an item in the list ... and print to the console
# first create new list of names
names = ["Tim", "Sarah", "Joe", "Matt", "Ben"]

print(names.index("Sarah"))  # 1
# print(names.index("John"))  # this will throw an error

# insert an item at index 2
names.insert(2, "Aaron")
print(names)

# sort based on ascii values
names.sort()
print(names)

names.extend(["billy", "sam", "sally", "mr. shoe", "Hammer"])
names.sort()
print(names)

# remove 'billy'
names.remove("billy")
print(names)

# use remove to try to remove bobby
# names.remove("bobby")  # this will throw an error
