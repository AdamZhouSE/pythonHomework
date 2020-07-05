n = int(input())
lists = []
for i in range(n):
    temp = list(map(int, input().split(",")))
    lists.append(temp)
#print(lists)

res = []
right = []
for i in range(lists.__len__()):
    arr = []
    subListright = lists[i][1]
    flag = False
    for j in range(lists.__len__()):
        if j == i:
            continue
        else:
            temp = []
            if lists[j][0] >= subListright:
                temp.append(lists[j][0])
                temp.append(j)
                arr.append(temp)
                flag = True

    #print(arr)
    if not flag:
        right.append(-1)
    else:
        arr.sort()
        right.append(arr[0][1])

print(right)