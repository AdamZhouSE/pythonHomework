num = int(input())
res = []
for i in range(num):
    list1 = input().split(" ")
    x = int(list1[0]) ^ int(list1[1])
    count = 1
    while x % 2 == 0:
        x = x >> 1
        count += 1
    res.append(count)
for i in res:
    print(i)