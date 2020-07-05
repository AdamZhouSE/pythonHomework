def func(arr:list,k:int,t:int):
    length=len(arr)
    for i in range(length):
        for j in range(i+1,length):
            if j-i<=k and abs(arr[i]-arr[j])<=t:
                return "true"
    return "false"
a=input()
b=a.index(']')
lists=list(map(int,a[8:b].split(',')))
k=int(a[b+7])
t=int(a[-1])
print(func(lists,k,t))