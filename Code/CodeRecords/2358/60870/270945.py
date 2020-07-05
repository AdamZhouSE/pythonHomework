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
    amount = info[1]
    array.sort(reverse = True)
    for j in range(0, amount):
        print(array[j], end = ' ')
    print()