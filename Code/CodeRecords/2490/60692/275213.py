list1 = input()[1:-1].split(",")
list2 = input()[1:-1].split(",")
res = []
if len(list1) > len(list2):
    list1, list2 = list2, list1
for i in list1:
    if list2.count(i) != 0:
        if res.count(i) == 0:
            res.append(i)
res = [int(j) for j in res]
res.sort()
print(res)