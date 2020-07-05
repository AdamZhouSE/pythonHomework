tests = int(input())
lists = []
for i in range(tests):
    arrSize = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)

res = []
for i in range(lists.__len__()):
    arr = lists[i]
    tempArr = []
    for j in range(arr.__len__()):
        for k in range(j+1, arr.__len__()):
            if arr[j] < arr[k]:
                tempArr.append(int(arr[k]) - int(arr[j]))
    #print(tempArr)
    maxSub = max(tempArr)
    res.append(maxSub)

#print(res)
for i in range(res.__len__()):
    print(res[i])