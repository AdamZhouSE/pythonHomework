n = int(input())
res = []
for i in range(n):
    list1 = []
    num = int(input())
    while num > 0:
        list1.append(str(num))
        num -= 5
    list2 = list1[:]
    list2.reverse()
    list1.append(str(num))
    list1 += list2
    res.append(" ".join(list1))
for i in res:
    print(i)