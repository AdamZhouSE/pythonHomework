tests = int(input())
lists = []
for i in range(tests):
    num = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)
#print(lists)
res = []
for k in range(lists.__len__()):
    temp = []
    for i in range(lists[k].__len__()-1):
        for j in range(i + 1, lists[k].__len__()):
            if int(lists[k][i]) < int(lists[k][j]):
                temp.append(int(j)-int(i))
    #print(temp)
    maxone = max(temp)
    res.append(maxone)

for i in range(res.__len__()):
    if i == res.__len__()-1:
        print(res[i])
    else:
        print(res[i], end=" ")