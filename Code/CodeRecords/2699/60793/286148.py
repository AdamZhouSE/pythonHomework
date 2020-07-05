from collections import Counter
from functools import cmp_to_key


def func(s1: str, s2: str):
    if s1 == s2:
        return 0
    if s1.startswith(s2):
        return 1
    if s2.startswith(s1):
        return -1
    for i in range(0, min(len(s1), len(s2))):
        if alphabet.index(s1[i]) < alphabet.index(s2[i]):
            return -1
        elif alphabet.index(s1[i]) > alphabet.index(s2[i]):
            return 1


ls = [input().strip() for x in range(0, int(input()))]
temp1 = [list(Counter(x).keys()) for x in ls]
alphabet = []
for x in temp1:
    alphabet = list(set(alphabet) | set(x))
#print(alphabet)
first = []
for x in range(0, len(alphabet)):
    ls = sorted(ls, key=cmp_to_key(func))
    first.append(ls[0])
    alphabet.append(alphabet[0])
    alphabet.remove(alphabet[0])
#print(first)
result = list(set(first))
print(len(result))
for x in ls:
    if x in result:
        print(x)

"""
4 
omm 
moo 
mom 
ommnom 
"""
