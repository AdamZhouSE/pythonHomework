def func(arr:list,k:int):
    length=len(arr)
    for i in range(1,length+1):
        for j in range(length+1-i):
            if sum(arr[j:j+i])>=k:
                return i

k=int(input())
a=input()
arr=list(map(int,a.split(',')))
print(func(arr,k))