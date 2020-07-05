num = int(input())
res = []
for i in range(num):
    n = int(input())
    list1 = [i for i in range(1, n + 1)]
    count = 0
    while n > 1:
        element = list1[0]
        list1.remove(list1[0])
        count += 1
        if count == 2:
            count = 0
            n -= 1
        else:
            list1.append(element)
    res.append(list1[0])
for i in res:
    print(i)