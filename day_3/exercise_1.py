# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
# Write a script that prompts the user to enter sidea, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
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
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

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