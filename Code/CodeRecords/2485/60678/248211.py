times = int(input())
for loopTimes in range(0, times):
    size = int(input())
    lists = input().split()
    for i in range(0, len(lists)):
        lists[i] = list(lists[i])
        lists[i].sort()
        lists[i] = ''.join(lists[i])

    countList = []

    while len(lists) > 0:
        tempCmp = lists[0]
        count = 0
        index = 0
        while index < len(lists):
            if lists[index] == tempCmp:
                count += 1
                del lists[index]
                index -= 1
            index += 1
        countList.append(str(count))
    print(' '.join(countList))
