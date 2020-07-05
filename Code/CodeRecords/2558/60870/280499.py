num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    list_ch = list(str_input)
    index = 0
    while index != len(list_ch):
        if list_ch[index] == '{':
            for j in range(index + 1, len(list_ch)):
                control = 0
                if list_ch[j] == '}':
                    del list_ch[index]
                    del list_ch[j - 1]
                    control = 1
                    break
            if control == 0:
                index = index + 1
        else:
            index = index + 1
    dict_cal = {'{':0, '}':0}
    for ch in list_ch:
        dict_cal[ch] = dict_cal[ch] + 1
    left = dict_cal['{']
    right = dict_cal['}']
    if (left + right) % 2 != 0:
        print(-1)
    else:
        if left % 2 != 0:
            print(int(left / 2) + int(right / 2) + 2)
        else:
            print(int(left / 2) + int(right / 2))