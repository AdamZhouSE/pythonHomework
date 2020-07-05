import collections
import re
pattern = re.compile('[0-9]+')
a = [int(x) for x in pattern.findall(input())]
n, m, c = a[0], a[1], a[2]
flag = True
a = [int(x) for x in pattern.findall(input())]
for i in range(len(a)-m+1):
    if max(a[i:i+m]) - min(a[i:i+m]) <= c:
        print(i+1)
        flag = False
if flag:
    print('NONE',end='')


