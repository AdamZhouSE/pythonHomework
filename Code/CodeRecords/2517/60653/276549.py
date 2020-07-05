import re
from collections import defaultdict
A = list([int(n) for n in re.findall(r"\-?\d+", input())])
B = list([int(n) for n in re.findall(r"\-?\d+", input())])
C = list([int(n) for n in re.findall(r"\-?\d+", input())])
D = list([int(n) for n in re.findall(r"\-?\d+", input())])
d1 = defaultdict(int)
for item1 in A:
    for item2 in B:
        d1[item1 + item2] += 1
d2 = defaultdict(int)
for item1 in C:
    for item2 in D:
        d2[item1+item2] += 1
count = 0
for item in d1.keys():
    if -item in d2:
        count += d1[item] * d2[-item]
print(count)