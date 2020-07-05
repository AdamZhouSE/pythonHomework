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
    for j in range(1, len(array) - 1):
        control = 0
        for k in range(0, j):
            if array[k] > array[j]:
                control = 1
        for k in range(j + 1, len(array)):
            if array[k] < array[j]:
                control = 1
        if control == 0:
            print(array[j])
            break
    if control == 1:
        print(-1)