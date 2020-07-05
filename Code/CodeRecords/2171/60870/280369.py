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
    array_odd = []
    array_even = []
    for ch in array:
        if ch % 2 == 0:
            array_even.append(ch)
        else:
            array_odd.append(ch)
    array_res = []
    if len(array_even) > 0:
        for ch in array_even:
            array_res.append(ch)
    if len(array_odd) > 0:
        for ch in array_odd:
            array_res.append(ch)
    for j in range(len(array_res)):
        if j == len(array_res) - 1:
            print(array_res[j])
        else:
            print(array_res[j], end = ' ')