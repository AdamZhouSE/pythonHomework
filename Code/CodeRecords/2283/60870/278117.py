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
    info = info_list[i]
    array = array_list[i]
    array.sort()
    for j in range(len(array)):
        if j != len(array) - 1:
            print(array[j], end = ' ')
        else:
            print(array[j], end = '')
    print()
