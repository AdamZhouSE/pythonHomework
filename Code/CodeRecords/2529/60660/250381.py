import collections
ori=collections.Counter(input())
ans=False
for b in range(31):
    tmp=collections.Counter(str(1<<b))
    if ori==tmp:
        ans=True
        break
print(str(ans).lower())