import collections

arr=input()
arr=arr[1:len(arr)-1]
arr=list(map(int,arr.split(',')))
count = collections.Counter()
counted = []
for x in arr:
    count[x] += 1
    counted.append((x, count[x]))
ans, cur = 0, (-1,-1)
for X, Y in zip(counted, sorted(counted)):
    cur = max(cur, X)
    if cur == Y:
        ans += 1
print(ans)