list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
res = []
for i in range(1, len(list1) + 1):
    if list1.count(i) == 2:
        res.append(i)
        break
for j in range(1, len(list1) + 1):
    if list1.count(j) == 0:
        res.append(j)
        break
print(res)