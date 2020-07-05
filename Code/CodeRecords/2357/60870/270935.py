num_test = int(input())
info_list = []
array1_list = []
array2_list = []
for i in range(num_test):
    info = input().split()
    array1 = input().split()
    array2 = input().split()
    info = [int(x) for x in info]
    array1 = [int(x) for x in array1]
    array2 = [int(x) for x in array2]
    info_list.append(info)
    array1_list.append(array1)
    array2_list.append(array2)
for i in range(num_test):
    info = info_list[i]
    array1 = array1_list[i]
    array2 = array2_list[i]
    goal = info[2]
    control = 0
    for num1 in array1:
        for num2 in array2:
            if num1 + num2 == goal:
                print(str(num1) + ' ' + str(num2))
                control = 1
    if control == 0:
        print(-1)