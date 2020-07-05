import re;
#from itertools import *
s = list([int(n) for n in re.findall(r"\d+", input())])
res = []
temp = 0
cnt = 0
for i in s:
    if i > temp:
        cnt += 1
    else:
        res.append(cnt)
        cnt = 0
    temp = i
print(max(res))