# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
import math


def evens_and_odds(nums):
    count_even = 0
    count_odd = 0
    for i in range(nums+1):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"The number of odds are {count_odd}.The number of evens are {count_even}.")

evens_and_odds(100)


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))

def is_empty(num):
    if num == 0:
        return True
    else:
        return False

print(is_empty(6))

def calculate_mean(nums):
    mean = sum(nums)/len(nums)
    return mean

nums = [1,2,3,4,5,5,5]
print(calculate_mean(nums))

def calculate_median(nums):
    median = nums[len(nums)//2]
    return median

print(calculate_median(nums))

def calculate_range(nums):
    mode=max(nums)-min(nums)
    return mode
print(calculate_range(nums))

def calculate_mode(nums):
    mode = nums.count(max(nums))
    return mode
print(calculate_mode(nums))

def calculate_variance(nums):
    mean = sum(nums)/len(nums)
    variance = sum((num-mean)**2 for num in nums)
    return variance

print(calculate_variance(nums))

def calculate_standard_deviation(nums):
    variance = calculate_variance(nums)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

print(calculate_standard_deviation(nums))

def greet(name="Guest"):
    return f"Hello,{name}!"

print(greet("Alice"))

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny

def show_args(**args):
    for key, value in args.items():
        print(f"{key}: {value}",end=" ")

show_args(name="Bob", pet="Fluffy, the bunny")
show_args(name="Alice", age=30, city="New York")