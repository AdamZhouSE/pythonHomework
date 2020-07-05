list_input = input()
list_input = list_input[2:len(list_input) - 2]
list_input = list_input.split("],[")
flag = int(input())
maximum = int(input())
max_distance = int(input())
res = []
for i in range(len(list_input)):
    list_temp = list_input[i].split(",")
    for j in range(len(list_temp)):
        list_temp[j] = int(list_temp[j])
    list_input[i] = list_temp
for i in range(len(list_input)):
    for j in range(len(list_input) - i - 1):
        if (10 - list_input[j][1]) > (10 - list_input[j + 1][1]):
            list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]
for i in range(len(list_input)):
    for j in range(len(list_input) - i - 1):
        if list_input[j][1] == list_input[j + 1][1]:
            if (len(list_input) - list_input[j][0]) > (len(list_input) - list_input[j + 1][0]):
                list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]
for i in range(len(list_input)):
    if flag == 1:
        if list_input[i][2] == flag and list_input[i][3] <= maximum and list_input[i][4] <= max_distance:
            res.append(list_input[i][0])
    if flag == 0:
        if list_input[i][3] <= maximum and list_input[i][4] <= max_distance:
            res.append(list_input[i][0])
print(res)
