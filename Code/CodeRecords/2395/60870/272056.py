def realign(opeList):
    zero_list = []
    goal_list = []
    for ele in opeList:
        if ele == 0:
            zero_list.append(ele)
        else:
            goal_list.append(ele)
    for k in range(len(zero_list)):
        goal_list.append(0)
    return goal_list


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
    control = 0
    while control == 0:
        control = 1
        for j in range(len(array) - 1):
            if array[j] == array[j + 1] and array[j] != 0:
                array[j] = 2 * array[j]
                array[j + 1] = 0
                control = 0
                break
        if control == 0:
            array = realign(array)
    for ch in array:
        print(str(ch), end = ' ')
    print()