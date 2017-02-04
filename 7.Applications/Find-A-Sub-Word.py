import re

# initialization
num_lines = int(input())
line_list = []
for i in range(num_lines):
    line = input()
    line_list.append(line)

num_query = int(input())
query_list = []
for i in range(num_query):
    query = input()
    query_list.append(query)

regex_pattern_line = re.compile(r'\W?\w+\W?')    
# find sub-words
for q in query_list:
    cnt = 0
    regex_pattern_query = re.compile(r'\w+' + q + '\w+')
    
    for l in line_list:
        finded_word_list = re.findall(regex_pattern_line, l)
        for w in finded_word_list:
            if re.search(regex_pattern_query, w):
                cnt += 1
                
    print(cnt)