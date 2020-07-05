def shuzu(a):
    l=0
    r=len(a)-1
    while l<r:
        mid=(r-l)//2+l
        if a[mid]==a[mid+1]:
            if (r-mid)%2==0:
                l=mid+2
            else:
                r=mid-1
        elif a[mid]==a[mid-1]:
            if (r-mid)%2==0:
                r=r-2
            else:
                l=mid+1
        else:
            return a[mid]
    return a[l]
a=eval(input())
print(shuzu(a))