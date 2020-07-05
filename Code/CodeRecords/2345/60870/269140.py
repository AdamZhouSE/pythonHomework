num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = int(input())
    array = input().split(' ')
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    info = info_list[i]
    array = array_list[i]
    dict_check = {}
    for ch in range(1, info + 1):
        dict_check[ch] = 0
    for ch in array:
        dict_check[ch] = dict_check[ch] + 1
    list_A = []
    list_B = []
    for ch in dict_check.keys():
        if dict_check[ch] == 0:
            list_A.append(ch)
        elif dict_check[ch] == 2:
            list_B.append(ch)
    list_A.sort()
    list_B.sort()
    if len(list_A) == 0 and len(list_B) > 0:
        print(str(list_B[0]) + ' ' + '0')
    elif len(list_A) > 0 and len(list_B) == 0:
        print('0' + ' ' + str(list_A[0]))
    elif len(list_A) == 0 and len(list_B) == 0:
        print('0 0')
    else:
        print(str(list_B[0]) + ' ' + str(list_A[0]))