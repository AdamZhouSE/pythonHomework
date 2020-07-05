def searchNum(aList, target):
    for i in aList:
        if i >= target:
            return alist.index(i)
    if aList[0] >= target:
        return 0
    else:
        return len(aList)


if __name__ == '__main__':
    alist = input().split(",")
    target = int(input())
    for i in range(len(alist)):
        alist[i] = int(alist[i])
    numIndex = searchNum(alist, target)
    print(numIndex)
