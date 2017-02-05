import re
import sys

regex_comment_pattern = r'/\*.*?\*/|//.*?$'
text = sys.stdin.read()
finded = re.findall(regex_comment_pattern, text, re.S|re.M)

for f in finded:
    f = re.sub(r'\n\s+', r'\n', f)
    print(f)