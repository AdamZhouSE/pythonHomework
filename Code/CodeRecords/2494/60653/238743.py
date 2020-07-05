import re;
#from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
ans = 0
for i in range(0, len(s)):
    for j in range(i+1, len(s)):
        if s[i] > s[j]*2:
            ans += 1
print(ans)