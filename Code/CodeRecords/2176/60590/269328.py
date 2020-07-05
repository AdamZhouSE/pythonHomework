str = input()
lists = list(str)
arr = []
for i in range(lists.__len__()):
    temp = []
    temp.append(lists[i])
    temp.append(i)
    arr.append(temp)
#print(arr)
arr.sort()
#print(arr)
for i in range(arr.__len__()):
    print(arr.__len__() - int(arr[i][1]), end=" ")