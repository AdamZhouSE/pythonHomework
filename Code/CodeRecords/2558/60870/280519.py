num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    dict_cal = {'{':0, '}':0}
    for ch in str_input:
        if ch == '{':
            dict_cal[ch] = dict_cal[ch] + 1
        elif ch == '}':
            if dict_cal['{'] != 0:
                dict_cal['{'] = dict_cal['{'] - 1
            else:
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