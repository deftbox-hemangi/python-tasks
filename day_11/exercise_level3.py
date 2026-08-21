# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(10))

def check_items(list12):
    return len(list12)==len(set(list12))

print(check_items([1,2,3,2,5]))

def check_datatype(list12):
    for item in list12:
        if type(item)!=type(list12[0]):
            return False
    else:
        return True
print(check_datatype([1,2,3,2,5]))

def check_variable(variable):
    return variable.isidentifier()

print(check_variable("-abc"))




