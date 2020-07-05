nums = int(input())
res = []
for i in range(nums):
    length = int(input())
    list1 = input().split(" ")
    list1 = [int(i) for i in list1]
    list1.sort()
    k = int(input())
    res.append(list1[k - 1])
for i in res:
    print(i)