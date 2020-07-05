def insertSort(list):
    point = 1
    while point < len(list):
        temp = list[point]
        tempPoint = point-1
        while tempPoint>-1:
            if(int(list[tempPoint]) > int(temp)):
                list[tempPoint+1] = list[tempPoint]
            else:
                list[tempPoint+1] = temp
                break
            tempPoint -= 1
        if tempPoint == -1:
                list[0] = temp
        point += 1
    return list

#main----------
source = input()
source = source[1:len(source)-1].split(',')
source = insertSort(source)

if len(source) < 2:
    print(0)
else:
    max = abs(int(source[1]) - int(source[0]))
    i = 1
    while i < len(source)-1:
        temp =abs(int(source[i+1]) - int(source[i]))
        if temp > max:
            max = temp
        i += 1
    print(max)
