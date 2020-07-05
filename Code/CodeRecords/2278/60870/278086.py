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
    res = []
    for j in range(len(array)):
        if j == len(array) - 1:
            res.append(array[j])
        else:
            temp = array[j] ^ array[j + 1]
            res.append(temp)
    for j in range(len(res)):
        if j != len(res) - 1:
            print(res[j], end = ' ')
        else:
            print(res[j], end = '')
    print()