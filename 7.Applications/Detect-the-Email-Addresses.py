import re

regex_pattern = r'\w+(\.\w+)*@\w+(\.\w+)*'

num_lines=int(input())
email_list = []
for i in range(num_lines):
    line=input()
    splited_line = re.split('(\w+(\.\w+)*@\w+(\.\w+)*)', line)
    
    for sub_line in splited_line:
        if sub_line:
            match = re.search(regex_pattern, sub_line)
            if match:
                email_list.append(str(match.group(0)))
            
print(";".join(sorted(set(email_list))))