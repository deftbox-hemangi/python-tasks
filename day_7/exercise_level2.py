# Exercises: Level 2
# Join A and B
# Find A intersection B
# Is A subset of B
# Are A and B disjoint sets
# Join A with B and B with A
# What is the symmetric difference between A and B
# Delete the sets completely

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B