def func(arr:list,k:int):
    res=False
    if arr.count(k)>0:
        res=True
    return res
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))