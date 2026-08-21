empty_list = []
print(empty_list)
print(type(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi','melon']
print(len(fruits))

print(fruits[0])
print(fruits[2])
print(fruits[5])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types=['Hemangi' ,23,172,False,'Ahmedabad']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0::2])

it_companies[1]='Tata'
print(it_companies)
it_companies[3]='Google'
print(it_companies)
print(it_companies[1].upper())

it_companies.append('#;  ')
print(it_companies)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3])
print(it_companies[-4:])
print(it_companies[4:6])
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack=front_end.copy()
new1=["Python","SQL"]
full_stack.extend(new1)
print(full_stack)




