s1, s2 = input(), input()
from itertools import permutations
l = [''.join(i) for i in permutations(s1)]
for i in range(len(s2) - len(s1) + 1):
    tmp = s2[i:i+len(s1)]
    if tmp in l:
        print(True)
        exit()
print(False)
