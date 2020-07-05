nums = int(input())
res = []
for i in range(nums):
    length = int(input())
    list1 = input().split(" ")
    list1 = [int(i) for i in list1]
    list1.sort()
    k = 0
    while k < len(list1) - 1:
        if list1[k] == list1[k + 1]:
            res.append(k + 1)
            break
        k += 1
    else:
        res.append(-1)
for i in res:
    print(i)