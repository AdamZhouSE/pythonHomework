import re;
from itertools import *
s = list([int(n) for n in re.findall(r"\-?\d+", input())])
odd = []
even = []
for i in s:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
for i in odd:
    even.append(i)
print(even)