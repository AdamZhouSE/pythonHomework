import collections
m = input().split(",")
count = collections.Counter(m)
X = min(count.values())
result = False
for x in range(2, X+1):
    if all(v % x == 0 for v in count.values()):
        result=True
        break
print(result)