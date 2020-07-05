#13
from itertools import permutations

n = int(input())
k = int(input())
nums = [str(i) for i in range(1,n+1)]
p = list(permutations(nums))
seq = []
for item in p:
    s = ""
    for num in item:
        s += num
    seq.append(s)
seq.sort()
print(seq[k-1])