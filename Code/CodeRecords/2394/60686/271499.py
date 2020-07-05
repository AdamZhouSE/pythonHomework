nums = int(input())
list_all = []
for i in range(nums):
    len_input = int(input())
    list_temp = input().split(" ")
    for j in range(len_input):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    list_temp = list_all[i]
    for j in range(len(list_temp) - 1):
        if list_temp[j] == 0:
            continue
    count = list_temp.count(0)
    res = []
    for j in range(len(list_temp)):
        if list_temp[j] != 0:
            res.append(list_temp[j])
    for j in range(count):
        res.append(0)
    for j in range(len(res)):
        print(res[j], end=" ")
    print()
