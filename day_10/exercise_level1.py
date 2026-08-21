# Iterate 0 to 10 using for loop, do the same using while loop.
#
# Iterate 10 to 0 using for loop, do the same using while loop.
#
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

for i in range(11):
    print(i,end="")
    print()

i=0
while i<11:
    print(i,end="")
    print()
    i=i+1

for i in range(10,-1,-1):
    print(i,end="")
    print()

i=10
while i>=0:
    print(i,end="")
    i=i-1

for i in range(8):
    print("#"*i,end="")
    print()
    print()


# Use nested loops to create the following:
#
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

#
# Use for loop to iterate from 0 to 100 and print only even numbers

for i in range(0,100,2):
    print(i,end=" ")
    print()
#
# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,100):
    if i%2==0:
        continue
    else:
        print(i,end=" ")
        print()

for i in range(9):
    print("#"*9,end=" ")
    print()

# Print the following pattern:
#
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100

for i in range(11):
    print(i ,"x", i, "=", i*i ,end="")
    print()

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list1=['Python', 'Numpy','Pandas','Django', 'Flask']

for list_item in list1:
    print(list_item)