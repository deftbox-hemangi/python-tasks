# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# Change the about food_stuff_tp tuple to a food_stuff_lt list
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_stuff_lt list
# Delete the food_stuff_tp tuple completely
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

fruits=('apple','banana','orange')
vegetables=('potato','carrot','banana')
animal_products=('paneer','milk','cheese')

food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

print(food_stuff_tp[4])
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])

del food_stuff_tp

# print(food_stuff_tp[2])

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
