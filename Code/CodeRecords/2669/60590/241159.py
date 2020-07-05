tests = int(input())

lists = []
for i in range(tests):
    n = int(input())
    lists.append(n)

result = []
for i in range(lists.__len__()):
    set1 = set()
    for j in range(lists[i]+1):
        temp1 = j&lists[i]
        set1.add(temp1)
        #print(set1)
    temp = list(set1)
    result.append(temp)

#print(result)
for i in range(result.__len__()):
    result[i].sort()

for i in range(result.__len__()):
    arr = result[i]
    for j in range(arr.__len__()):
        if j==arr.__len__()-1:
            print(arr[arr.__len__()-1-j], end=" ")
            print()
        else:
            print(arr[arr.__len__()-1-j], end=" ")

