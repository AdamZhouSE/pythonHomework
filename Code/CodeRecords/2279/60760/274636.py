def func(arr:list,sum:int):
    length=len(arr)
    res=[]
    for i in range(length):
        for j in range(1,length-i):
            temp=arr[i:j+i]
            he=0
            for m in temp:
                he=he+m
            if he==sum:
                res.append(i+1)
                res.append(j+i)
                return res
    if res==[]:
        res.append(-1)
    return res
tests=int(input())
lists=[]
sums=[]
for i in range(tests):
    sums.append(list(map(int,input().split(" ")))[1])
    lists.append(list(map(int,input().split(" "))))
results=[]
for i in range(tests):
    results.append(func(lists[i],sums[i]))
for i in results:
    for j in i:
        print(j,end=" ")
    print()
