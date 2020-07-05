def func(arr:list,k:int):
    
    return arr.index(k)
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))