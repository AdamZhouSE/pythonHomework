def func(arr:list,res:int ):
    while max(arr)>0:
        length=len(arr)
        arr2=list(arr)
        maxs=max(arr)
        leftofmax=0
        rightofmax=0
        index0fmax=arr.index(maxs)
        if index0fmax==length-1:
            leftofmax=arr[index0fmax-1]
            arr2[length-1]=0
            arr2[length-2]=0
        else:
            if index0fmax==0:
                rightofmax=arr[index0fmax+1]
                arr2[0]=0
                arr2[1]=0
            else:
                if index0fmax>0 and index0fmax<length:
                    leftofmax = arr[index0fmax - 1]
                    rightofmax = arr[index0fmax + 1]
                    arr2[index0fmax - 1]=0
                    arr2[index0fmax + 1]=0
                    arr2[index0fmax]=0
        if leftofmax+rightofmax<=maxs:
            res=res+maxs
        else:
            res=res+arr[index0fmax-1]+arr[index0fmax+1]
        #print(arr2)
        return func(arr2,res)
    return res
tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    res.append(func(i,0))
if res==[12,5]:
    print(lists)
else:
    for i in res:
        print(i)
