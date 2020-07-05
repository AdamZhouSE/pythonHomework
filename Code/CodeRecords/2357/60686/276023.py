nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    length1, length2, res = (int(x) for x in input().split(" "))
    list_num.append(res)
    list_temp1 = input().split(" ")
    for j in range(length1):
        list_temp1[j] = int(list_temp1[j])
    list_all.append(list_temp1)
    list_temp2 = input().split(" ")
    for j in range(length2):
        list_temp2[j] = int(list_temp2[j])
    list_all.append(list_temp2)
for i in range(nums):
    list_temp1 = list_all[i * 2]
    list_temp2 = list_all[i * 2 + 1]
    res = list_num[i]
    for j in range(len(list_temp1)):
        for k in range(len(list_temp2)):
            if list_temp1[j] + list_temp2[k] == res:
                print(list_temp1[j],end=" ")
                print(list_temp2[k])