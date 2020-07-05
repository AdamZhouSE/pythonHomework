nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list_all.append(num)
for i in range(nums):
    num = list_all[i]
    list_temp = []
    sum = 0
    for j in range(1, num + 1):
        if num % j == 0:
            if list_temp.count(j) == 0:
                list_temp.append(j)
            if list_temp.count(num) == 0:
                list_temp.append(num / j)
        else:
            continue
    for j in range(len(list_temp)):
        sum += list_temp[j]
    if sum < num * 2:
        print(1)
    else:
        print(0)
