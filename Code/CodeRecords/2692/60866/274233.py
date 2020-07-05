def panduan(a,k):
    l=0
    temp=0
    d=0
    while l<len(a):
        temp=temp+a[l]
        if temp>k:
            temp=0
            d=d+1
        elif temp==k:
            l=l+1
            temp=0
            d=d+1
        else:
            l=l+1
    if temp>0:
        d=d+1
    return d
def shuzu(weights,d):
    l=max(weights)
    r=sum(weights)
    while l<=r:
        mid=(r-l)//2+l
        if panduan(weights,mid)>d:
            l=mid+1
        else:
            r=mid-1
    return l
weights=eval(input())
d=int(input())
print(shuzu(weights,d))