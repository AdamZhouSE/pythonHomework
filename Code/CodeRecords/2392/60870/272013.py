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
    array = array_list[i]
    goal = info_list[i][1]
    control = 0
    for j in range(0, len(array) - 1):
        for k in range(j + 1, len(array)):
            if array[j] * array[k] == goal:
                control = 1
    if control == 1:
        print('Yes')
    else:
        print('No')