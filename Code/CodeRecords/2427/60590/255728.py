tests = int(input())
lists = []
for i in range(tests):
    arrSize = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)
#print(lists)

arr1 = []
for i in range(lists.__len__()):
    arr = lists[i]
    temp = []
    for j in range(arr.__len__()):
        for k in range(j+1, arr.__len__()):
            if arr[j] == arr[k]:
                temp.append(arr[j])
    arr1.append(temp)
#print(arr1)

res = []
for i in range(lists.__len__()):
    arr2 = lists[i]
    repeat = arr1[i]
    if repeat == []:
        res.append([-1])
    else:
        temp = []
        for j in range(arr2.__len__()):
            for k in range(repeat.__len__()):
                if arr2[j] == repeat[k]:
                    temp.append(j+1)
        res.append(temp)

#print(res)
for i in range(res.__len__()):
    print(res[i][0])