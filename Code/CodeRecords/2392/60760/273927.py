def func(arr:list,x:int):
    length=len(arr)
    for i in range(length):
        for j in range(length):
            if j>i and arr[i]*arr[j]==x:
                return 'Yes'
    return 'No'
tests=int(input())
lists=[]
xs=[]
for i in range(tests):
    xs.append(list(map(int,input().split(" ")))[1])
    lists.append(list(map(int,input().split(" "))))

for i in range(tests):
    print(func(lists[i],xs[i]))