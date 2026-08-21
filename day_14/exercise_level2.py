from operator import truediv
from os import MFD_ALLOW_SEALING

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Marshall Islands",
    "Netherlands",
    "New Zealand",
    "Poland",
    "Solomon Islands",
    "Switzerland",
    "Thailand"]


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li=["Hemangi",2,"Patel","abc"]

def to_upper(s):
    return s.upper()

list_upper=(list(map(to_upper, names)))
print(list_upper)

list_upper=(list(map(to_upper, countries)))
print(list_upper)

def squares(num):
    return num**2

sq_nums=(list(map(squares, numbers)))
print(sq_nums)

def filter_country(country):
    return "land" in country

land_country=(list(filter(filter_country, countries)))
print(land_country)

def country_letter(country):
    return len(country)==6

country_letter=(list(filter(country_letter, countries)))
print(country_letter)

def country1_letter(country):
    return len(country)>=6

country1_letter=(list(filter(country1_letter, countries)))
print(country1_letter)

def filter_country_e(country):
    return "e" in country

filter_country_e=(list(filter(filter_country_e, countries)))
print(filter_country_e)

def get_string_lists(list1):
    return list(filter(lambda x: isinstance(x, str), li))

print(get_string_lists(li))

from functools import *
def sum_num(x,y):
    return int(x)+int(y)

total=reduce(sum_num,numbers)
print(total)

def conatenate_country(a,b):
    return a+","+b

result=reduce(conatenate_country,countries[:-1])
print(result+" and " + countries[-1]+" are north European countries")

from day_10 import *

def categorize_country(pattern):
    return list(filter(lambda country:pattern in country.lower(), countries))

print(categorize_country("land"))

from collections import Counter

def count_letter_with_samecountry_name(country):
    return dict(Counter(country[0].lower() for country in countries))

print(count_letter_with_samecountry_name(countries))

def get_first_ten_countries(country):
    return country[:10]

print(get_first_ten_countries(countries))

def get_last_ten_countries(country):
    return country[-10:]

print(get_last_ten_countries(countries))

def sort_countries(countries):
    return sorted(countries)

print(sort_countries(countries))


