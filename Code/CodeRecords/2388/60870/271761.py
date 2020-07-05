num_test = int(input())
info_list = []
array1_list = []
array2_list = []
for i in range(num_test):
    info = int(input())
    array1 = input().split()
    array2 = input().split()
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    array1_list.append(array1)
    array2_list.append(array2)
for i in range(num_test):
    dict1 = {}
    dict2 = {}
    array1 = array1_list[i]
    array2 = array2_list[i]
    for ch in array1:
        if ch in dict1.keys():
            dict1[ch] = dict1[ch] + 1
        else:
            dict1[ch] = 1
    for ch in array2:
        if ch in dict2.keys():
            dict2[ch] = dict2[ch] + 1
        else:
            dict2[ch] = 1
    if dict1 == dict2:
        print(1)
    else:
        print(0)