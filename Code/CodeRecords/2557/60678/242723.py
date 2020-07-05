times = int(input())


for i in range(0, times):
    numInput2List = list(input())

    index = 0
    while index <  len(numInput2List)-1:
        if numInput2List[index] == numInput2List[index + 1]:
            del numInput2List[index]
            index -= 1
        index += 1
    print(''.join(numInput2List))