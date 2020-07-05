nums = int(input())
list_all = []
for i in range(0, nums):
    length = int(input())
    list_temp = input().split(" ")
    for j in range(length):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    list_temp = list_all[i]
    sum1 = 0
    sum2 = 0
    for j in range(0, len(list_temp), 2):
        sum1 += list_temp[j]
    for j in range(1, len(list_temp), 2):
        sum2 += list_temp[j]
    print(max(sum1, sum2))
