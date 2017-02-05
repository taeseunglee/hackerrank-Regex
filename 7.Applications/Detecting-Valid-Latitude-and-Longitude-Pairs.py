import re

regex_pattern = r'\(([+-]?(\d|[1-9]\d)(\.[0-9]+)?), ([+-]?(\d|[1-9]\d|[1-9]\d\d)(\.?[0-9]+)?)\)'
num_lines = int(input())

for nl in range(num_lines):
    line = input()
    match = re.search(regex_pattern, line)
    
    try:
        valid = True
        latitude = float(match.group(1))
        longitude = float(match.group(4))
        if not ((-90 <= latitude) and (latitude <= 90)):
            valid = False
        if not ((-180 <= longitude) and (longitude <= 180)):
            valid = False
    except (ValueError, AttributeError):
        valid = False

    if valid:
        print("Valid")
    else:
        print("Invalid")