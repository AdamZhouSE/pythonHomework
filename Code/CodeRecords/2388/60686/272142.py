nums = int(input())
list_all = []

for i in range(nums):
    len_input = int(input())
    list_temp_1 = input().split(" ")
    for j in range(len_input):
        list_temp_1[j] = int(list_temp_1[j])
    list_all.append(list_temp_1)
    list_temp_2 = input().split(" ")
    for j in range(len_input):
        list_temp_2[j] = int(list_temp_2[j])
    list_all.append(list_temp_2)
for i in range(nums):
    flag = True
    list_temp_1 = list_all[i * 2]
    list_temp_2 = list_all[2 * i + 1]
    list_temp_1.sort()
    list_temp_2.sort()
    for j in range(len(list_temp_1)):
        if list_temp_2[j] != list_temp_1[j]:
            flag = False
            break
    if flag:
        print(1)
    else:
        print(0)

