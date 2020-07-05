import collections

S = str(input())
T = str(input())
count = collections.Counter(T)
res = []

for c in S:
    res.append(c * count[c])
    count[c] = 0

for c in count:
    res.append(c * count[c])

result = "".join(res)
print(result)