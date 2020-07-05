n = int(input())
list1 = []
res = []
for i in range(n):
    list1.append(input().split(","))
if len(list1) == 1:
    res.append(-1)
    print(res)
else:
    list2 = list1[:]
    list2.sort()
    for i in list1:
        index = list2.index(i)
        if index == len(list2) - 1:
            res.insert(list1.index(i), -1)
        else:
            if i[1] <= list2[index + 1][0]:
                res.insert(list1.index(i), list1.index(list2[index + 1]))
            else:
                res.insert(list1.index(i), -1)
    print(res)