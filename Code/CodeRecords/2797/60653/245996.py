import re;
from itertools import *
#s = list([int(n) for n in re.findall(r"\-?\d+", input())])
n = int(input())
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
if n < 1:
    print(-1)
elif n == 1:
    if s[0] == 0:
        print("UP")
    elif s[0] == 15:
        print("DOWN")
    else:
        print(-1)
elif n == 2:
    if s[1] == 0 or s[0] < s[1] < 15:
        print("UP")
    else:
        print("DOWN")
elif s[n - 1] == 15:
    print("DOWN")
elif max(s) == s[n-1]:
    print("UP")
elif s[n-2] < s[n-1] < 15:
    print("UP")
elif s[n-1] == 0:
    print("UP")
else:
    print("DOWN")