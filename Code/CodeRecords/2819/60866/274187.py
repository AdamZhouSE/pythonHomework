def shuzu(a):
    a.sort()
    ans=0
    l=0
    r=len(a)-1
    while r-l>=1:
        if a[l]+a[r]>4:
            r=r-1
            ans=ans+1
        elif a[l]+a[r]==4:
            l=l+1
            r=r-1
            ans=ans+1
        elif a[l]+a[r]<4:
            sum=a[l]+a[r]
            while sum<4:
                l=l+1
                sum=sum+a[l]
            if sum==4:
                l=l+1
                r=r-1
                ans=ans+1
            else:
                r=r-1
                ans=ans+1
    if l==r:
        ans=ans+1
    return ans
n=input()
a=input()
a=a.split(' ')
a=[int(x) for x in a]
b=shuzu(a)
print(b)