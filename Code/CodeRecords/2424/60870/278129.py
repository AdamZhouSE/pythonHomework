num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    array = array_list[i]
    dict_array = {}
    for ch in array:
        if ch in dict_array.keys():
            dict_array[ch] = dict_array[ch] + 1
        else:
            dict_array[ch] = 1
    for ch in dict_array.keys():
        if dict_array[ch] % 2 != 0:
            print(ch)
            break