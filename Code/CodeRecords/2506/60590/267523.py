lists = list(map(int, input().split(",")))

arr = []
for i in range(lists.__len__()):
    len = 1
    temp = lists[i]
    for j in range(i+1, lists.__len__()):
        if lists[j] > temp:
            len += 1
            temp = lists[j]
    arr.append(len)
print(max(arr))