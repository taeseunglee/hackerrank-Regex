import re

regex_pattern = r'^[_.]\d+[a-zA-Z]*_?$'

num_lines = int(input())

for n in range(num_lines):
    line = input()
    match = re.search(regex_pattern, line)

    if match:
        print("VALID")
    else:
        print("INVALID")