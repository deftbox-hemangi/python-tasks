import random, string

def random_user_id():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
print(random_user_id())


# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number
# of IDs which are supposed to be generated.

def user_id_gen_by_user():
    charas=int(input("Enter number of characters how long you want the userID: "))
    nums=int(input("Enter number of id you want to generate: "))

    for i in range(nums):
        user_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(charas))

        print(user_id)

user_id_gen_by_user()

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

def rgb_color_gen():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

print(rgb_color_gen())
