nums = int(input())
list_all = []
list_num = []
for i in range(nums):
    len_input = int(input())
    list_temp = input().split(" ")
    for j in range(len_input):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
    res = int(input())
    list_num.append(res)
for i in range(nums):
    flag = True
    list_temp = list_all[i]
    res = list_num[i]
    for j in range(0, len(list_temp) - 3):
        for k in range(j + 1, len(list_temp) - 2):
            for l in range(k + 1, len(list_temp) - 1):
                for m in range(l + 1, len(list_temp)):
                    if list_temp[j] + list_temp[k] + list_temp[l] + list_temp[m] == res:
                        print(1)
                        exit(-1)

    print(0)
