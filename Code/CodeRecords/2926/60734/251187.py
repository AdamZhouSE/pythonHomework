n = int(input())
lst = list(map(int,input().split()))
maxCount = 0
for x in list(set(lst)):
    maxCount = max(maxCount,lst.count(x))
print(maxCount)