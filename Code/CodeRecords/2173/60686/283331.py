nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list_all.append(num)
for i in range(nums):
    num = list_all[i]
    sum = 0
    for j in range(1, num + 1):
        sum += j * j
    print(sum)
