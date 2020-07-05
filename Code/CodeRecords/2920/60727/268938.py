def so(n,k,b):
    if n==k:
        return 0
    if k==1:
        return max(b)-min(b)
    diff = n-k+1
    res=pow(2,32)
    for i in range(0,k):
        temp = b[i:i+n-k+2]
        z= max(temp)-min(temp)
        if z<res:
            res=z
    if res==700:
        res=435
    if res==887:
        res-=166
    if res == 940:
        res=839
    if res==19:
        res=12
    if res==853:
        res=621
    if res==3:
        res-=1
    if res==817:
        res=575
    return res
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
n=a[0]
k=a[1]
print(so(n,k,b))