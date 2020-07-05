num_test = int(input())
info_list = []
array_list = []
goal_list = []
for i in range(num_test):
    info = int(input())
    array = input().split()
    array = [int(x) for x in array]
    goal = int(input())
    info_list.append(info)
    array_list.append(array)
    goal_list.append(goal)
for i in range(num_test):
    array = array_list[i]
    goal = goal_list[i]
    control = 0
    for x1 in range(0, len(array) - 3):
        for x2 in range(x1 + 1, len(array) - 2):
            for x3 in range(x2 + 1, len(array) - 1):
                for x4 in range(x3 + 1, len(array)):
                    if array[x1] + array[x2] + array[x3] + array[x4] == goal:
                        control = 1
    print(control)