def nums_22_leastMove(list = []):
    list = sorted(list)
    sumN = 0
    for item in list:
        sumN += item-list[int(len(list)/2)] if (item > list[int(len(list)/2)]) else list[int(len(list)/2)] - item
    print(sumN)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_22_leastMove(list)