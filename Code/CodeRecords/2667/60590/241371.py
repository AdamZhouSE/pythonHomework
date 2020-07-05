tests =int(input())
lists = []
for i in range(tests):
    temp = list(map(int, input().split()))
    lists.append(temp)

#print(lists)
for i in range(lists.__len__()):
    arr = lists[i]
    str=""
    for j in range(arr[1]):
        str = str + "1"
    #print(str)
    stores = pow(2, str.__len__())-1
    #print(stores)
    left = stores-arr[0]+1
    print(left)
