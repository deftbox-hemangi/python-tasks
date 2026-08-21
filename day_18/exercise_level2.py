import re

def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, name))

print(is_valid_variable("$$578"))
print(is_valid_variable("first"))
