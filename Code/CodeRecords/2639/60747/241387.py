
s=input()
k=int(input())
from collections import defaultdict

hash = defaultdict(int)
start = 0
maxCount = 0
res = 0
for i in range(len(s)):
    hash[s[i]] += 1
    maxCount = max(maxCount, hash[s[i]])
    while i - start + 1 - maxCount > k:
        hash[s[start]] -= 1
        maxCount = max(maxCount, hash[s[start]])
        start += 1
    res = max(i - start + 1, res)
print(res)