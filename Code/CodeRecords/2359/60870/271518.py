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
    count = 0
    array = array_list[i]
    for j in range(0, len(array) - 1):
        for k in range(j + 1, len(array)):
            if array[j] + array[k] in array:
                count = count + 1
    if count == 0:
        print(-1)
    else:
        print(count)