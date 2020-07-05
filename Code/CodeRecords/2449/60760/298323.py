def func(arr:list,k:int):

    return str(arr).find(str(k))
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))