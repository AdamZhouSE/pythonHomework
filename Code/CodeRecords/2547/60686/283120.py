nums = int(input())
list_all = []
for i in range(nums):
    length = int(input())
    input_list = input().split(" ")
    for j in range(length):
        input_list[j] = int(input_list[j])
    num = int(input())
    list_all.append(input_list)
    list_all.append(num)
for i in range(nums):
    input_list = list_all[i * 2]
    num = list_all[i * 2 + 1]
    list_res = []
    list_temp1 = []
    list_temp2 = []
    for j in range(len(input_list) - 1):
        for k in range(j + 1, len(input_list)):
            if abs(input_list[j] - input_list[k]) == num:
                list_temp1.append(input_list[j])
                list_temp1.append(input_list[k])
                list_temp2.append(input_list[k])
                list_temp2.append(input_list[j])
                if list_res.count(list_temp1) == 0 and list_res.count(list_temp2) == 0:
                    list_res.append(list_temp1)
                    list_res.append(list_temp2)
                    list_temp1 = []
                    list_temp2 = []
                else:
                    list_temp1 = []
                    list_temp2 = []
    print(int(len(list_res) / 2))
