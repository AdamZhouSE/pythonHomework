num=eval(input())
def MaxMid(num,l,r):
    mid=(l+r)//2
    lmax=-99999999
    rmax=-99999999
    lsum=0
    rsum=0
    for i in range(mid,-1,-1):
        lsum+=num[i]
        if lsum>lmax:
            lmax=lsum
    for i in range(mid+1,r+1):
        rsum+=num[i]
        if rsum>rmax:
            rmax=rsum
    return max(lmax,rmax,lmax+rmax)
def MaxSubArray(num,l,r):
    mid=(l+r)//2
    if(l==r):
        return num[l]
    lmax=MaxSubArray(num,0,mid)
    rmax=MaxSubArray(num,mid+1,r)
    mmax=MaxMid(num,l,r)
    return max(lmax,rmax,mmax)
print(MaxSubArray(num,0,len(num)-1))