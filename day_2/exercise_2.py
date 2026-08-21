# Check the data type of all your variables using type() built-in function
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


help(total)

r=30
pi=3.141592653589793

ar = pi * r ** 2
print("Radius : " , ar)

circumference = 2 * pi * r
print("Circumference : ",circumference)

rd=int(input("Enter the radius of the circumference : "))
area = pi * rd **2
print("Area of the circle : " , area)


f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")
age1 = int(input("Enter your age : "))
country1 = input("Enter your country : ")

print(f_name,l_name,age1,country1)