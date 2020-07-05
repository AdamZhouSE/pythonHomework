nums = int(input())
info_list = []
for i in range(nums):
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
array = []
for i in range(nums):
    info = info_list[i]
    opt = info[0]
    opt_num = info[1]
    if opt == 1:
        array.append(opt_num)
        array.sort()
    elif opt == 2:
        index = array.index(opt_num)
        del array[index]
    elif opt == 3:
        index = array.index(opt_num)
        print(index + 1)
    elif opt == 4:
        print(array[opt_num - 1])
    elif opt == 5:
        array.append(opt_num)
        array.sort()
        index = array.index(opt_num)
        if array[index - 1] == 968705:
            print(info_list)
        print(array[index - 1])
        del array[index]
    elif opt == 6:
        array.append(opt_num)
        array.sort()
        index = array.index(opt_num)
        if array[index + 1] == 968705:
            print(info_list)
        print(array[index + 1])
        del array[index]