numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

zeroes = [x for x in numbers if x<=0]
print(zeroes)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

li=[num for row in list_of_lists for num in row]
print(li)

new_li=[(i, "1",i, i*2, i*3, i*4, i*5) for i in range(11)]
print(new_li)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_lis=[[country.upper() , country[:3].upper(), city.upper()] for [(country,city)] in countries]
print(new_lis)

new_list=[{"country": country.upper(), "city": city.upper()} for [(country,city)] in countries]
print(new_list)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list2 = [[first_name, last_name] for [(first_name, last_name)] in names]
print(new_list2)

square = (lambda x:x**2)
print(square(4))