nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    num = int(input())
    list_all.append(str_input)
    list_all.append(num)
for i in range(nums):
    str_input = list_all[i * 2]
    num = list_all[i * 2 + 1]
    maximum = 0
    for j in range(len(str_input), 0, -1):
        for k in range(len(str_input) - j + 1):
            list_temp = []
            str_temp = str_input[k: k + j]
            for m in range(j):
                if list_temp.count(str_temp[m]) == 0:
                    list_temp.append(str_temp[m])
            if len(list_temp) == num and len(list_temp) > maximum:
                maximum = j
    print(maximum)
