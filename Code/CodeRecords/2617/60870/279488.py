num_test = int(input())
info_list = []
for i in range(num_test):
    info = input().split()
    info_list.append(info)
for i in range(num_test):
    info = info_list[i]
    str_input = str(info[0])
    num = int(info[1])
    count = 0
    for j in range(len(str_input)):
        for k in range(j + 1, len(str_input) + 1):
            dict_num = {}
            for p in range(j, k):
                if str_input[p] not in dict_num:
                    dict_num[str_input[p]] = 1
                else:
                    dict_num[str_input[p]] = dict_num[str_input[p]] + 1
            if '1' not in dict_num.keys():
                pass
            elif dict_num['1'] == num:
                count = count + 1
    print(count)