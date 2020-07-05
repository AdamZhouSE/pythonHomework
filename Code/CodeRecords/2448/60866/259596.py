def paixu(a):
    a.sort()
    l=len(a)
    lo=0
    hi=l-1
    res=0
    while(lo<hi):
        mid=lo+(hi-lo)//2
        cnt=l-mid
        if a[mid]>=cnt:
            res=cnt
            hi=mid-1
        else:
            lo=mid+1
    print(res)
a=input()
a=eval(a)
paixu(a)