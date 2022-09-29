def student_info(**kwargs):  # the convention is to use **kwargs
    return f"{kwargs['name']}, age {kwargs['age']}, has a {kwargs['GPA']} GPA."


student_1 = {
    "name": "Timothy Unkert",
    "age": 46,
    "GPA": 4.0,
    "is_male": True
}

print(student_info(**student_1))

# play with this!
