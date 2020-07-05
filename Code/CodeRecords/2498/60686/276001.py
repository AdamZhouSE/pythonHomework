str_input = input()
str_input = str_input[1:len(str_input) - 1]
list_int = str_input.split(",")
for i in range(len(list_int)):
    list_int[i] = int(list_int[i])
flag_list = []
for i in range(len(list_int)):
    if (i + list_int[i]) % 2 != 0:
        if len(flag_list) == 0:
            flag_list.append(i)
        else:
            list_int[flag_list[0]], list_int[i] = list_int[i], list_int[flag_list[0]]
print(list_int)
