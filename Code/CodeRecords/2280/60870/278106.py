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
    info = info_list[i]
    array = array_list[i]
    control = 0
    for j in range(len(array)):
        if array[j] != j + 1:
            print(j + 1)
            control = 1
            break
    if control == 0:
        print(info)