def func(arr:list,k:int):
    res=[]
    for i in range(len(arr)):
        if arr[i]==k:
            return i
        if arr[i]>k:
            return i-1
    
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))