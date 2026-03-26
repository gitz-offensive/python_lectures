#!usr/bin/python
"""Use python3 to do execution"""""

def casing_function(text):
    return text.lower()


def getting_it():
    name = casing_function("Mr. Gitau")
    if name.islower():
        print(name)
        print("Cool Working")
    else:
        print("Name is not Lowercase")


getting_it()