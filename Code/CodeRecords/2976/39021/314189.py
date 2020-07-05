import re
import sys
s = input()
list = sys.stdin.readlines()
for i in range(len(list)-1):
    print((re.sub(s,'',list[i],flags=re.IGNORECASE)).replace(' ',''),end='')
print((re.sub(s,'',list[len(list)-1],flags=re.IGNORECASE)).replace(' ',''))

