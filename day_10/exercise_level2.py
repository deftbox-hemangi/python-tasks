res=0
for i in range(0,101):
    res+=i
print("Sum of all Numbers is:  ",res)

sum_even=0
sum_odd=0
for i in range(0,101):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i

print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")
