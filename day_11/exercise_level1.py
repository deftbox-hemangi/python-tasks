# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
import math


def sum_nums(num1,num2):
    return num1+num2

print(sum_nums(2,3))

def area_of_circle(radius):
    return math.pi*radius**2
print(area_of_circle(5))

def add_all_nums(*nums):
    return sum(nums)

print(add_all_nums(3,4,56,6))

def convert_celsius_to_fahrenheit(degrees):
    return degrees*9/5+32

print(convert_celsius_to_fahrenheit(10))

def check_season(month):
    if month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['January', 'February', 'December']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    else:
        return "Incorrect"

print(check_season('September'))

def calculate_slope(x, y):
    return math.atan(y/x)
print(calculate_slope(1, 2))


def solve_quadratic_eqn(a,b,c):
    return a*b + c

print(solve_quadratic_eqn(1, 2, 3))


def print_list(lst):
    print(lst)

lst = [1,2,3,4,5,6]
print_list(lst)

def reverse_list(lst):
    return lst[::-1]

print(reverse_list(lst))
print(reverse_list(["A", "B", "C"]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def capitalize_list_items(list1):
    return [item.capitalize() for item in list1]

print(capitalize_list_items(['ninja', 'smell']))


def add_item(list12,add_new):
        list12.append(add_new)
        return list12

print(add_item([1,2,3,4,5,6], 37))

def remove_item(food_stuff,remove_new):
    food_stuff.remove(remove_new)
    return food_stuff

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff,"Potato"))

def remove_item(numbers,remove_new):
    numbers.remove(remove_new)
    return numbers


numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(num1):
    sum = 0
    for i in range(num1+1):
        sum+=i
    return sum

print(sum_of_numbers(10))


def sum_of_odds(nums):
    total = 0
    for i in range(nums+1):
        if i%2!=0:
            total+=i
        else:
            continue
    return total

print(sum_of_odds(5))

def sum_of_evens(nums):
    total = 0
    for i in range(nums+1):
        if i%2==0:
            total+=i
        else:
            continue
    return total

print(sum_of_evens(5))