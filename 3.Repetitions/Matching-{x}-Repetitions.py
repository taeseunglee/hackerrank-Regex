Regex_Pattern = '^[(a-z)(A-Z)(02468)]{40}[\s13579]{5}$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())