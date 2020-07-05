def func(arr:list,k:int):
    res=[]
    for i in arr:
        if i==k:
            res.append(arr.index(i))
    if len(res)<2:
        res=[-1,-1]
    return res
a=input()
k=int(input())
arr=list(map(int,a.split(',')))
print(func(arr,k))