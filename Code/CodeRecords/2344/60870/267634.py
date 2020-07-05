num_test = int(input())
info_list = []
array_list = []
distance_list = []
for i in range(num_test):
    info = int(input())
    array = input().split(' ')
    array = [int(x) for x in array]
    distance = int(input())
    info_list.append(info)
    array_list.append(array)
for i in range(num_test):
    array_goal = []
    array = array_list[i]
    for j in range(0, len(array), distance):
        array_temp = []
        if j + distance > len(array):
            for k in range(j, len(array)):
                array_temp.append(array[k])
        else:
            for k in range(j, j + distance):
                array_temp.append(array[k])
        array_goal.append(array_temp)
    value = array_goal[0]
    for j in range(len(array_goal) - 1):
        array_goal[j] = array_goal[j + 1]
    array_goal[-1] = value
    for j in range(len(array_goal)):
        for ch in array_goal[j]:
            print(ch, end = ' ')
    print()