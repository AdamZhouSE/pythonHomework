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
    for j in range(0, len(array), 2):
        if j + 1 >= len(array):
            pass
        else:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
    for j in range(len(array)):
        if j == len(array) - 1:
            print(array[j])
        else:
            print(array[j], end = ' ')