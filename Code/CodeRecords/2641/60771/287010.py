#13
from itertools import permutations

s1 = input()
s2 = input()
l = list(permutations(s1,len(s1)))
# print(l)
flag = False
for item in l:
    if "".join(item) in s2:
        flag = True
        break
print(flag)