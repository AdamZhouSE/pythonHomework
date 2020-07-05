def func(arr:list,k:int):
    if arr[-1]<k:
        return len(arr)
    res=[]
    for i in range(len(arr)):
        if arr[i]>=k:
            return i

a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))