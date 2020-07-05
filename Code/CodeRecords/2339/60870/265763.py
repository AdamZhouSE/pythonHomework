num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input()
    array = input().split(' ')
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    info = info_list[i]
    info = [int(x) for x in info]
    array = array_list[i]
    array = [int(x) for x in array]
    count = 0
    for j in range(len(array) - 1):
        for k in range(j + 1, len(array)):
            if array[j] > array[k]:
                count = count + 1
    print(count)