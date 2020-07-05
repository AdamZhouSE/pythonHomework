lists = list(map(int, input().split(",")))
maxNum = max(lists)
base = []
for i in range(0, maxNum+1):
    base.append(i)
set1 = set(lists)
set2 = set(base)
res = set2.difference(set1)
res = list(res)
print(res[0])