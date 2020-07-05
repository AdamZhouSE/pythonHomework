n = int(input())
k = int(input())
l = []
for i in range(1, n+1):
    l.append(str(i))
from itertools import permutations
tmp = permutations(''.join(l))
print(tmp[k])
