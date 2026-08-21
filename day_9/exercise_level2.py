# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F

score=int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print("Your grade is D")
elif 0 <= score <= 59:
    print("Your grade is F")
else:
    print("Invalid Score entered")


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer

month=input("Enter month: ")

if month in ['September', 'October', 'November']:
    print("The season is Autumn")
elif month in ['January', 'February', 'December']:
    print("The season is Winter")
elif month in ['March', 'April', 'May']:
    print("The season is Spring")
elif month in ['June', 'July', 'August']:
    print("The season is Summer")
else:
    print("Check the Month AGAIN")


# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

your_fruits = input("Enter your fruit: ")
if your_fruits in fruits:
    print( f"{your_fruits} already EXISTS!")
else:
    fruits.append(your_fruits)
    print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }


if 'skills' in person:
    print(person['skills'][2])
    if 'Python' in 'skills':
        print(person['skills'])

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

# if 'skills' in person:
#     if ['JavaScript','React'] in 'skills':
#         print("He is a front end developer")
#     elif ['Node', 'Python', 'MongoDB'] in 'skills':
#         print('He is a backend developer')
#     elif ['React', 'Node','MongoDB'] in 'skills':
#         print('He is a fullstack developer')
#     else:
#         print("Unknown title")
# else:
#     print("Have fun you got no Skills")


if person['is_married']==True:
    if person['country']=='Finland':
        print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
