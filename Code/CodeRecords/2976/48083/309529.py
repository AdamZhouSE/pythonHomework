import sys
import re

s = input()
code = ''
for i in sys.stdin:
    if i != '':
        code += i

code = re.sub(s, '', code, flags=re.IGNORECASE)
code = re.sub(' ','',code)
print(code)