# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
import types

age = [22, 19, 24, 25, 26, 24, 25, 24]

ages=set(age)
print(ages)

# String and tuple are immutable data types.
# list is mutable data type and ordered in nature
# set is unordered mutable data type

str_1="I am a teacher and I love to inspire and teach people"
new_str_1=str_1.split()
print(new_str_1)

new_set=set(new_str_1)
print(new_set)
print("Unique words : ",len(new_set))