# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random
def shuffle_list(l):
    random.shuffle(l)
    return l

print(shuffle_list([1,2,3,4,5,6]))

def array_of_list():
    return ''.join(set(random.choice('0123456789') for i in range(7)))

print(array_of_list())