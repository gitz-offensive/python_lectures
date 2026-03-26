
"""# list
numbers = [1, 2, 3, 4, 5]
print(numbers)

# add items
numbers.append(6)
print(numbers)

numbers.remove(3)
print(numbers)

print(numbers[2])


"""


# dictionary
user = {
    "name": "Gitau",
    "age": 20,
    "city" : "Nairobi",
    "weight" : 70.2
}

# Access the values
print(user["city"])

# update /add
user["Home_city"] = "Mombasa"

del user["age"]

print(user)