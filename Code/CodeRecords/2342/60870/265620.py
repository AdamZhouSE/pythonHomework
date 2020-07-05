num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input().split(' ')
    array = input().split(' ')
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    info = info_list[i]
    array = array_list[i]
    info = [int(x) for x in info]
    array = [int(x) for x in array]
    distance = info[1]
    array_temp_list = []
    for j in range(0, len(array), distance):
        array_temp = []
        if j + distance > len(array):
            for k in range(j, len(array)):
                array_temp.append(array[k])
        else:
            for k in range(j, j + distance):
                array_temp.append(array[k])
        array_temp_list.append(list(reversed(array_temp)))
    for j in range(len(array_temp_list)):
        for k in range(len(array_temp_list[j])):
            print(array_temp_list[j][k], end = ' ')
    print()