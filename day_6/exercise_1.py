# Create an empty tuple
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# Join brothers and sisters tuples and assign it to siblings
# How many siblings do you have?
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# Unpack siblings and parents from family_members

t1=()
print(type(t1))

brothers=('python','sql','java','js')
print(brothers)

sisters=('HTML','CSS')
print(sisters)

siblings=brothers+sisters
print(siblings)

print(len(siblings))

parents=('Dad','Mom')
family_members=siblings+parents
print(family_members)

*siblings,father,mother=family_members
print("Siblings : ",siblings)
print("Father",father)
print("Mother",mother)
