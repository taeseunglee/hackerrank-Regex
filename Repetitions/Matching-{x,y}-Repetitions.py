Regex_Pattern = '^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())