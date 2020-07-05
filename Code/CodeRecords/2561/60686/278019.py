nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    length, res = (int(x) for x in input().split(" "))
    list_num.append(res)
    list_temp2 = []
    for j in range(length):
        list_temp = input().split(" ")
        for k in range(length):
            list_temp[k] = int(list_temp[k])
        list_temp2.extend(list_temp)
    list_all.append(list_temp2)
    list_temp1 = []
    for j in range(length):
        list_temp = input().split(" ")
        for k in range(length):
            list_temp[k] = int(list_temp[k])
        list_temp1.extend(list_temp)
    list_all.append(list_temp1)
for i in range(nums):
    list_temp1 = list_all[i * 2]
    list_temp2 = list_all[i * 2 + 1]
    res = list_num[i]
    count = 0
    for j in range(len(list_temp1)):
        for k in range(len(list_temp2)):
            if list_temp1[j] + list_temp2[k] == res:
                count += 1
    print(count)
