import re

num_lines = int(input())
regex_domain_pattern = r'https?://(www2?\.)?[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+'
domain_list = []

for nl in range(num_lines):
    line = input()
    finded = re.findall('https?://(www2?\.)?([a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)+)', line)

    for f in finded:
        domain_list.append(f[1])


print(";".join(sorted(set(domain_list))))