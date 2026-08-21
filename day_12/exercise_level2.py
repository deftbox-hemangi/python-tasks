import random,string

def list_of_hexa_colors():
    return '#' + ''.join(random.choice('abcdef0123456789') for _ in range(6))

print(list_of_hexa_colors())

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
# Write a function generate_colors which can generate any number of hexa or rgb colors.

def list_of_rgb_colors():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r,g,b

print(list_of_rgb_colors())

def generate_colors(n):
    return '#' + ''.join(random.choice('abcdef0123456789') for i in range(n))

print(generate_colors(8))