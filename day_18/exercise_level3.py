import re
from collections import Counter


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned_text = re.sub(r'[^A-Za-z ]', '', sentence)

words = cleaned_text.split()
count = Counter(words)

print(cleaned_text)
print(count.most_common(3))