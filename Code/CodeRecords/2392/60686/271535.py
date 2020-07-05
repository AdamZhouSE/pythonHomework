nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    len_input, temp = (int(x) for x in input().split(" "))
    list_num.append(temp)
    list_temp = input().split(" ")
    for j in range(len_input):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for i in range(nums):
    flag = False
    list_temp = list_all[i]
    number = list_num[i]
    for j in range(len(list_temp)):
        for k in range(j, len(list_temp)):
            if list_temp[j] * list_temp[k] == number and j != k:
                flag = True
    if flag:
        print("Yes")
    else:
        print("No")
