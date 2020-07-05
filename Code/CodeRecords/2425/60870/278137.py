num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input().split()
    array = input().split()
    info = [int(x) for x in info]
    array = [int(x) for x in array]
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    info = info_list[i]
    array = array_list[i]
    base = info[1]
    minDiffer = abs(array[0] - base)
    index = 0
    for j in range(1, len(array)):
        if abs(array[j] - base) <= minDiffer:
            minDiffer = abs(array[j] - base)
            index = j
    print(array[index])