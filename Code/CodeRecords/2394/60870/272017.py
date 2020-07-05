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
    zero_list = []
    goal_list = []
    for ch in array:
        if ch == 0:
            zero_list.append(ch)
        else:
            goal_list.append(ch)
    for j in range(len(zero_list)):
        goal_list.append(0)
    for j in range(len(goal_list)):
        if j == len(goal_list) - 1:
            print(str(goal_list[j]))
        else:
            print(str(goal_list[j]), end = ' ')