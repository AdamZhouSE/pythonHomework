def realign(opeList):
    zero_list = []
    goal_list = []
    for ch in opeList:
        if ch == 0:
            zero_list.append(ch)
        else:
            goal_list.append(ch)
    for i in range(len(zero_list)):
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
    for j in range(len(array) - 1):
        if array[j] == array[j + 1] and array[j] != 0:
            array[j] = array[j] * 2
            array[j + 1] = 0
    array = realign(array)
    for ch in array:
        print(str(ch), end = ' ')
    print()