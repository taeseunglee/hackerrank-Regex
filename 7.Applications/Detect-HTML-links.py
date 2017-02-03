import re

regex_pattern = r'a.*?href="([^"]*)".*?>(.*?)</a>'
num_lines=int(input())

for i in range(num_lines):
    line=input()

    splited_line = re.split('(<a.*?href="[^"]*".*?>.*?</a>)', line)
    
    for sub_line in splited_line:
        match = re.search(regex_pattern, sub_line)

        if match:
            href = str(match.group(1))
            text = str(match.group(2))
            text = str(re.sub('<[^>]+>', '', text)).lstrip()
            print(href + "," + text)