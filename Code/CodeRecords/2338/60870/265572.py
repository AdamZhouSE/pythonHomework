num_test = int(input())
info_list = []
array_list = []
for i in range(num_test):
    info = input().split(' ')
    array = input().split(' ')
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    goal = int(info_list[i][1])
    array = array_list[i]
    array = [int(x) for x in array]
    control = 0
    for j in range(len(array) - 1):
        for k in range(j + 1, len(array)):
            if array[j] + array[k] == goal:
                print('Yes')
                control = 1
                break
    if control == 0:
        print('No')