def func(arr:list,k:int):
    res=-1
    if arr.count(k)>0:
        res=arr.index(k)
    return res
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))