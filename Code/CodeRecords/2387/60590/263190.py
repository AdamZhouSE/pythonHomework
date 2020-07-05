arrSize, localSorttimes = map(int, input().split())
lists = list(map(int, input().split()))
localSort = []
for i in range(localSorttimes):
    temp = list(map(int, input().split()))
    localSort.append(temp)
index = int(input())
#print(lists)
#print(localSort)

def riseSort(lists, localArr):
    res = lists.copy()
    left = int(localArr[1])
    right = int(localArr[2])
    temp = lists[left-1: right]
    temp.sort()
    for i in range(left-1, right):
        res[i] = temp[i-left+1]
    return res

def sinkSort(lists, localArr):
    res = lists.copy()
    left = int(localArr[1])
    right = int(localArr[2])
    temp = lists[left-1: right]
    temp.sort()
    temp.reverse()
    for i in range(left-1, right):
        res[i] = temp[i-left+1]
    return res

for i in range(localSorttimes):
    if localSort[i][0] == 0:
        lists = riseSort(lists, localSort[i])
        #print(lists)
    else:
        lists = sinkSort(lists, localSort[i])
        #print(lists)

print(lists[index-1])