def func(arr:list,sum:int):
    length=len(arr)
    res=[]
    for i in range(length):
        for j in range(1,length-i+1):
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
if results[0]==-1:
    print(lists)
    print(sums)
for i in results:
    for j in range(len(i)-1):
        print(i[j],end=" ")
    print(i[len(i)-1])
