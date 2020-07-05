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
    count = 0
    for j in range(len(array)):
        for k in range(j + 1, len(array) + 1):
            dict_test = {}
            control = 0
            for p in range(j, k):
                if array[p] not in dict_test.keys():
                    dict_test[array[p]] = 1
                else:
                    dict_test[array[p]] = dict_test[array[p]] + 1
            for ch in dict_test.keys():
                if dict_test[ch] > 1:
                    control = 1
                    break
            if control == 1:
                break
            else:
                for ch in dict_test.keys():
                    count = count + 1
    print(count)