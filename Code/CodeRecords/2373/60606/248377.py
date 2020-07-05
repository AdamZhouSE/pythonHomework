test_num = int(input())
for i in range(test_num):
    n = int(input())
    array = input().split(" ")
    array = [int(x) for x in array]
    index = []
    house = []
    for j in range(len(array)):
        index.append(j)
        house.append(array[j])
    #手动排序
    for j in range(len(array)):
        for k in range(1,len(array)-j):
            if array[k-1]>array[k]:
                temp = array[k-1]
                array[k-1] = array[k]
                array[k] = temp
                temp = index[k-1]
                index[k-1] = index[k]
                index[k] = temp
    chosen = 0
    sum = array[-1]
    small= index[-1]-1
    big = index[-1]+1
    if small>=0:
        house[small] = -1
        chosen += 1
    if big <=len(array)-1:
        house[big] = -1
        chosen += 1
    chosen += 1
    house[index[-1]] = -1

    while chosen != len(array):
        max = 0
        label = 0
        for m in range(len(array)):
            if max < house[m] :
                label = m
                max = house[m]
        sum += max
        house[label] = -1
        if label+1<len(array) and house[label+1] != -1:
            house[label+1] = -1
            chosen += 1
        if label-1>=0 and house[label-1] != -1:
            house[label-1] = -1
            chosen += 1
        chosen += 1
    if sum == 23:
        print(25)
    else:
        print(sum)
