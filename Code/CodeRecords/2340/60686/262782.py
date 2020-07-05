def find_max(index, list_t):
    maximum = min(max(list_t[0:index]), max(list_t[index + 1: len(list_t)]))
    return maximum


def judge(list_input, num):
    water_sum = 0
    for a in range(1, num - 1):
        water_temp = find_max(a, list_input) - list_input[a]
        if water_temp < 0:
            water_temp = 0
        water_sum += water_temp
    print(water_sum)


n = int(input())
list_all = []
list_num = []
for i in range(n):
    temp_num = int(input())
    list_num.append(temp_num)
    list_temp = input().split(" ")
    for j in range(temp_num):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
for x in range(n):
    judge(list_all[x], list_num[x])
