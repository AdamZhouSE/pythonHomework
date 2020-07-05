num_test = int(input())
str_list = []
info_list = []
for i in range(num_test):
    str_input = input()
    info = int(input())
    str_list.append(str_input)
    info_list.append(info)
for i in range(num_test):
    str_input = str_list[i]
    info = info_list[i]
    valid_list = []
    for j in range(len(str_input)):
        for k in range(j + 1, len(str_input) + 1):
            dict_ch = {}
            temp = str_input[j:k]
            for p in range(len(temp)):
                if temp[p] not in dict_ch.keys():
                    dict_ch[temp[p]] = 1
                else:
                    dict_ch[temp[p]] = dict_ch[temp[p]] + 1
            if len(dict_ch) == info:
                res = 0
                for ch in dict_ch.keys():
                    res = res + dict_ch[ch]
                valid_list.append(res)
    maxLen = max(valid_list)
    print(maxLen)
