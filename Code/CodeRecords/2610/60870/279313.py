num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    array = [int(x) for x in array]
    array_list.append(array)
    info_list.append(info)
for i in range(num_test):
    array = array_list[i]
    dict_valid = {}
    for j in range(len(array)):
        for k in range(j + 1, len(array) + 1):
            dict_test = {}
            for p in range(j, k):
                if array[p] not in dict_test.keys():
                    dict_test[array[p]] = 1
                else:
                    dict_test[array[p]] = dict_test[array[p]] + 1
            res = sorted(dict_test.items(), key = lambda dict_test:dict_test[0])
            dict_test = dict(res)
            res_str = str(dict_test)
            res_len = 0
            for ch in dict_test.keys():
                res_len = res_len + dict_test[ch]
            if res_str in dict_valid.keys():
                pass
            else:
                dict_valid[res_str] = res_len
    res = 0
    for ch in dict_valid.keys():
        res = res + dict_valid[ch]
    print(res)
    if res == 9:
        print(array)