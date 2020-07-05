num_test = int(input())
info_list = []
array1_list = []
array2_list = []
for i in range(num_test):
    info = input().split()
    array1 = input().split()
    array2 = input().split()
    info = [int(x) for x in info]
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    info_list.append(info)
    array1_list.append(array1)
    array2_list.append(array2)
for i in range(num_test):
    array1 = array1_list[i]
    array2 = array2_list[i]
    array_res = []
    for ch in array1:
        array_res.append(ch)
    for ch in array2:
        array_res.append(ch)
    array_res.sort()
    for ch in array_res:
        print(str(ch), end = ' ')
    print()