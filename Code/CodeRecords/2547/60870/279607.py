num_test = int(input())
info_list = []
array_list = []
diff_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    diff = int(input())
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
    diff_list.append(diff)
for i in range(num_test):
    info = info_list[i]
    array = array_list[i]
    diff = diff_list[i]
    dict_res = {}
    for j in range(len(array) - 1):
        for k in range(j + 1, len(array)):
            if abs(array[j] - array[k]) == diff:
                temp = [array[j], array[k]]
                sorted(temp)
                str_temp = str(temp)
                if str_temp in dict_res:
                    dict_res[str_temp] = dict_res[str_temp] + 1
                else:
                    dict_res[str_temp] = 1
    if dict_res is None:
        print(0)
    else:
        count = 0
        for ch in dict_res.keys():
            count = count + 1
        print(count)