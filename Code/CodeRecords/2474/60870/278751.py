num_test = int(input())
str_list = []
for i in range(num_test):
    str_input = input()
    str_list.append(str_input)
for i in range(num_test):
    str_input = str_list[i]
    valid_dict = {}
    for j in range(len(str_input)):
        res = 0
        for k in range(j, len(str_input) - 1, 2):
            if str_input[k] == '(' and str_input[k + 1] == ')':
                res = res + 2
        valid_dict[res] = 1
    maxLen = max(valid_dict.keys())
    print(maxLen)