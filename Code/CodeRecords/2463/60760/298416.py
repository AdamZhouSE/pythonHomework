def func(arr:list,k:int):
    res=[]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==k:
                res.append(i+1)
                res.append(j+1)
    if len(res)==0:
        res=None
    return res[0:2]
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))