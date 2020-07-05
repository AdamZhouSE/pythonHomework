def func(arr:list,k:int):
    arr2=sorted(arr)
    return arr2[-k]
a=input()
k=int(input())
arr=list(map(int,a[1:len(a)-1].split(',')))
print(func(arr,k))