#Day 2: 30 Days of python programming
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it
# Declare a variable is_light_on and assign a value to it
# Declare multiple variable on one line

first_name = "Hemangi"
last_name = "Patel"
full_name = "Hemangi Patel"
country = "India"
city = "Ahmedabad"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True

one,two,three = 1,2,3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(one))
print(type(two))
print(type(three))



# Using the len() built-in function, find the length of your first name
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
# Add num_one and num_two and assign the value to a variable total
# Subtract num_two from num_one and assign the value to a variable diff
# Multiply num_two and num_one and assign the value to a variable product
# Divide num_one by num_two and assign the value to a variable division
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
# Calculate num_one to the power of num_two and assign the value to a variable exp
# Find floor division of num_one by num_two and assign the value to a variable floor_division
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print("Compare string : ",(len(first_name) == (len(last_name))))


num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)


# help(total)

r=30
pi=3.141592653589793

ar = pi * r ** 2
print("Radius : " , ar)

circumference = 2 * pi * r
print("Circumference : ",circumference)

rd=int(input("Enter the radius of the circumference : "))
area = pi * rd **2
print("Area of the circle : " , area)


# f_name = input("Enter your first name : ")
# l_name = input("Enter your last name : ")
# age1 = int(input("Enter your age : "))
# country1 = input("Enter your country : ")
#
# print(f_name,l_name,age1,country1)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).



age2 = 34
h = 5.8
comp = 1 + 4j

print(comp)

base=int(input("Enter the base : "))
height=int(input("Enter the Height : "))

area_of_triangle = 0.5 * base * height
print("Area of the triangle : " , area_of_triangle)

a=int(input("Enter the side A : "))
b=int(input("Enter the side B : "))
c=int(input("Enter the side C : "))

perimeter = (a+b+c)/2

print("Perimeter of the triangle : " , perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

length=int(input("Enter the length : "))
width = int(input("Enter the width : "))
area3 = length * width
perimeter2 = 2 * (length + width)
print("Area of the triangle : " , area3)
print("Perimeter of the triangle : " , perimeter2)

x=int(input("Enter the x : "))

y = (2 * x -2)

print(y)

import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope)
print("Euclidean distance:", distance)


print(len("Python"))
print(len("Dragon"))

if len("Python") == len("Dragon"):
    print("The length of the string is NOT equal to the length of the other string")

if "on" in "Python" and "Dragon":
    print("Found")


new1="I hope this course is not full of jargon"

if "jargon" in new1:
    print("Found")

if "on" not in "Python" and "Dragon":
    print("Not Found")

py=len("Python")
py1=float(py)
py2=str(py)

n=6
if n%2==0:
    print("Even")
else:
    print("Odd")


new2=7//3
print(new2)

new3=int(2.7)

if new2==new3:
    print("Equal")


new4=str('10')
print(new4==10)

new5=int(9.8)
print(new5==10)

hours=int(input("Enter the hours : "))
rate=int(input("Enter the Rate per hour : "))

print("Rate per hours : ",hours*rate)



years = int(input("Enter number of years : "))

seconds = years * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")


for i in range(1, 6):
    print(i, 1, i, i**2, i**3)


# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
t="Thirty"
d="Days"
o="Of"
p="Python"
print(t+" "+d+" "+o+" "+p)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

c="Coding "
f="For "
al="All "
print(c+f+al)
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

company="Coding for All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[:6])


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(text.split(" "))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

# What is the character at index 0 in the string Coding For All.
print(text[0])

# What is the last index of the string Coding For All.
print(len(text) - 1)

# What character is at index 10 in "Coding For All" string.
print(text[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent="You cannot end a sentence with because because because is a conjunction"
print(sent.find("because"))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.rindex("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent.find("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
# Does 'Coding For All' end with a substring coding?
print(company.endswith("Coding"))


# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
com='   Coding For All      '
print(com.strip())



# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

web = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(web)
print(result) # 'HTML# CSS# JavaScript# React'


