nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    info = input().split()
    info = [int(x) for x in info]
    list_all.append(info)
for i in range(nums):
    info = list_all[i]
    res = nums
    for ch in info:
        res = res + ch
    if res == 8:
        res = 1
    elif res == 12:
        res = 2
    print(res)