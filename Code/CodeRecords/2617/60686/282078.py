nums = int(input())
list_all = []
for i in range(nums):
    str_list = input().split(" ")
    list_all.append(str_list[0])
    list_all.append(int(str_list[1]))
for i in range(nums):
    str_input = list_all[i * 2]
    num = list_all[i * 2 + 1]
    count = 0
    for j in range(num, len(str_input) + 1):
        for k in range(0, len(str_input) - j + 1):
            if str_input[k:k + j].count('1') == num:
                count += 1
    print(count)
