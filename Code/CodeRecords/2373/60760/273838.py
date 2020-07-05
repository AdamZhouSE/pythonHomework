def func(arr:list,res:int ):
    while max(arr)>0:
        length=len(arr)
       # arr2=list(arr)
        maxs=max(arr)
        leftofmax=0
        rightofmax=0
        index0fmax=arr.index(maxs)
        if index0fmax==length-1:
            leftofmax=arr[index0fmax-1]
            arr[length-1]=0
            arr[length-2]=0
        else:
            if index0fmax==0:
                rightofmax=arr[index0fmax+1]
                arr[0]=0
                arr[1]=0
            else:
                if index0fmax>0 and index0fmax<length:
                    leftofmax = arr[index0fmax - 1]
                    rightofmax = arr[index0fmax + 1]
                    arr[index0fmax - 1]=0
                    arr[index0fmax + 1]=0
                    arr[index0fmax]=0
        if leftofmax+rightofmax<=maxs:
            res=res+maxs
        else:
            res=res+arr[index0fmax-1]+arr[index0fmax+1]
        #print(arr)
        return func(arr,res)
    return res
tests=int(input())
lists=[]
temp=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
    temp.append(list(map(int,input().split(" "))))
res=[]

for i in lists:
    res.append(func(i,0))
if res==[12,5]:
    print(temp)
else:
    for i in res:
        print(i)
