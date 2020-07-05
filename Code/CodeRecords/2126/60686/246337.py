list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
list_result = [list_input[0]]
for i in range(1, len(list_input)):
    flag = True
    for j in range(len(list_result)):
        if list_input[i] % list_result[j] != 0:
            flag = False
    if flag:
        list_result.append(list_input[i])
print(list_result)