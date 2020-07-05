num = int(input())
res = []
for i in range(num):
    list1 = input().split(" ")
    n = int(list1[0])
    x = int(list1[1])
    if x < 10:
        res.append((n - 1) * (10 - x))
    else:
        res.append(0)
for i in res:
    print(i)