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
    array_goal = sorted(array)
    for j in range(len(array) - 1):
        minNum = array[j]
        index = j
        for k in range(j + 1, len(array)):
            if array[k] < minNum:
                minNum = array[k]
                index = k
        if index != j:
            count = count + 1
            temp = array[index]
            array[index] = array[j]
            array[j] = temp
            if array == array_goal:
                break
    print(count)