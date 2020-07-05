def func(arr:list,k:int):
    res=[]
    for i in range(len(arr)):
        if arr[i]==k:
            res.append(i)
    if len(res)==1:
        res=res+res
    if len(res)==0:
        res=[-1,-1]
    return res
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))