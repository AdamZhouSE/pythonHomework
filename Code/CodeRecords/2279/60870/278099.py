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
    goal = info[1]
    start = 0
    end = 0
    control = 0
    for j in range(len(array)):
        for k in range(j + 1, len(array) + 1):
            res = 0
            for p in range(j, k):
                res = res + array[p]
            if res == goal:
                start = j + 1
                end = k
                control = 1
                break
        if control == 1:
            break
    if start == 0 and end == 0:
        print(-1)
    else:
        print(str(start) + ' ' + str(end))