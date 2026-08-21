import re
from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)
word_count = Counter(words)

print(word_count)

text = '''
The position of some particles on the horizontal x-axis are -12, -4, -3
and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
'''

points1 = re.findall(r'-?\d+', text)

points=sorted(map(int,points1))
distance = points[-1] - points[0]
print(points)
print(distance)
