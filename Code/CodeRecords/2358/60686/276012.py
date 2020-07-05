nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    length, res = (int(x) for x in input().split(" "))
    list_num.append(res)
    list_temp = input().split(" ")
    for j in range(length):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    list_temp = list_all[i]
    res = list_num[i]
    list_temp.sort()
    for j in range(-1, -1 - res , -1):
        print(list_temp[j], end=" ")
    print()
