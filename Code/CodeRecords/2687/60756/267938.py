import math
T=int(input())
arr=["1"]
for t in range(T):
    n=int(input())
    ans=[]
    k=math.ceil(math.log(n,2))
    while len(arr)<k:
        arr.append(arr[-1]+str((len(arr)-1)%2))
    for i in range(k):
        num=int(arr[i],2)
        if num<=n:
            ans.append(str(num))
    print(' '.join(ans))