tests = int(input())
lists = []
for i in range(tests):
    arrSize = int(input())
    temp = list(map(int, input().split()))
    lists.append(temp)

res = []
for i in range(lists.__len__()):
    arr = lists[i]
    odd = []
    even = []
    temp = []
    for j in range(arr.__len__()):
        if arr[j] % 2 ==0:
            even.append(arr[j])
        else:
            odd.append(arr[j])
    odd.sort()
    odd.reverse()
    even.sort()
    odd.extend(even)
    res.append(odd)

#print(res)
for i in range(res.__len__()):
    if i != 0:
        print()
    for j in range(res[i].__len__()):
        print(res[i][j], end=" ")
print()
