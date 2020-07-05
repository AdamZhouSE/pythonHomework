num_test = int(input())
info_list = []
array_list1 = []
array_list2 = []
for i in range(num_test):
    info = input().split(' ')
    array1 = input().split(' ')
    array2 = input().split(' ')
    info_list.append(info)
    array_list1.append(array1)
    array_list2.append(array2)
for i in range(num_test):
    info = info_list[i]
    array1 = array_list1[i]
    array2 = array_list2[i]
    info = [int(x) for x in info]
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    order = info[2]
    array_temp = []
    for ch in array1:
        array_temp.append(ch)
    for ch in array2:
        array_temp.append(ch)
    array_temp.sort()
    print(array_temp[order - 1])