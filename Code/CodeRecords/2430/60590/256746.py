tests = int(input())
lists = []
for i in range(tests):
    arrSize = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)
    temp1 = []
    k = int(input())
    lists.append(k)
#print(lists)

res = []
for i in range(0, lists.__len__(), 2):
    flag = False
    tempArr = []
    tempArr1 = []
    arr = lists[i]
    sum = lists[i+1]
    for j in range(arr.__len__()):
        for k in range(j+1, arr.__len__()):
            if int(arr[j]) + int(arr[k]) == sum:
                flag = True
                tempArr.append(arr[j])
                tempArr.append(arr[k])
                tempArr.append(sum)
                tempArr1.append(tempArr)
                tempArr = []
    if not flag:
        res.append([-1])
    else:
        res.append(tempArr1)
#print(res)
for i in range(res.__len__()):
    arr = res[i]
    if i!=0:
        print()
    if arr == [-1]:
        print(-1, end="")
    else:
        for j in range(arr.__len__()):
            if j!=0:
                print()
            for k in range(arr[0].__len__()):
                if k == arr[0].__len__()-1:
                    print(arr[j][k], end="")
                else:
                    print(arr[j][k], end=" ")
print()

