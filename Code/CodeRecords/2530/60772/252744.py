import collections

S = input()
T = input()
count = collections.Counter(T)
res = []
for item in S:
    res.append(item*count[item])
    count[item] = 0
for item in count:
    res.append(item*count[item])

print("".join(res))
