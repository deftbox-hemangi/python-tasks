# reate an empty dictionary called dog
# Add name, color, breed, legs, age to the dog dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

dog={}
print(type(dog))

dog={"name":"dog",'color':'red','breed':'German Shepherd','age':22,'legs':3}
print(dog)

student_dict={'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }}

print(len(student_dict))

print(student_dict['skills'])

student_dict['skills'].extend(['Native','HTML'])

print(student_dict['skills'])

print(student_dict.keys())
print(student_dict.values())

print(student_dict.items())

student_dict.pop('skills')
print(student_dict)

del dog 