# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# Cut(slice) out the first word of Coding For All string.
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# Replace the word coding in the string 'Coding For All' to Python.
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
# Split the string 'Coding For All' using space as the separator (split()) .
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# What is the character at index 0 in the string Coding For All.
# What is the last index of the string Coding For All.
# What character is at index 10 in "Coding For All" string.
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Create an acronym or an abbreviation for the name 'Coding For All'.
# Use index to determine the position of the first occurrence of C in Coding For All.
# Use index to determine the position of the first occurrence of F in Coding For All.
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does 'Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python


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

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
print(f"radius = 10\narea = 3.14 \"* radius **\" 2\nThe area of a circle with radius 10 is 314 meters square.")