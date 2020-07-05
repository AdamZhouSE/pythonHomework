nums = int(input())
res = []
for i in range(nums):
    length = int(input())
    list1 = input().split(" ")
    list1 = [int(i) for i in list1]
    max_num = 0
    for m in range(len(list1) - 1):
        for n in range(m + 1, len(list1)):
            if list1[m] < list1[n] and list1[n] - list1[m] > max_num:
                max_num = list1[n] - list1[m]
    if max_num == 0:
        res.append(-1)
    else:
        res.append(max_num)
for i in res:
    print(i)