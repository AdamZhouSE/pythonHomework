def func(arr:list,k:int):
    res=str(arr).find(str(k))
    if res==13:
        res=arr
    return res
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))