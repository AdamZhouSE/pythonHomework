lists = list(map(int, input().split(",")))

res = []
for i in range(lists.__len__()):
    for j in range(i+1, lists.__len__()):
        if lists[i] == lists[j]:
            res.append(lists[i])
            break
#print(res)
set1 = set(lists)
base = []
for i in range(lists.__len__()):
    base.append(i+1)
set2 = set(base)
missing = set2.difference(set1)
missing = list(missing)
res.append(missing[0])
print(res)