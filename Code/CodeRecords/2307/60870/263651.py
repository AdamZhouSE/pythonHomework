num_test = int(input())
array_list = []
for i in range(num_test):
    size = int(input())
    array = input().split(' ')
    array_list.append(array)
for i in range(len(array_list)):
    array = array_list[i]
    size = len(array)
    dict_array = {}
    for num in array:
        if num not in dict_array:
            dict_array[num] = 1
        else:
            dict_array[num] = dict_array[num] + 1
    res = -1
    for key in dict_array.keys():
        if dict_array[key] > int(size / 2):
            res = int(key)
    print(res)