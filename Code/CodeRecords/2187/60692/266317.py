num = int(input())
res = []
for i in range(num):
    k = int(input().split(" ")[1])
    list1 = input().split(" ")
    list1 = [int(i) for i in list1]
    max = 0
    for m in range(len(list1) - k + 1):
        if sum(list1[m: m + k]) > max:
            max = sum(list1[m: m + k])
    res.append(max)
for i in res:
    print(i)