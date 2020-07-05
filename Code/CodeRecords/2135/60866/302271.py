def shuzi(a):
    a.sort()
    l=0
    r=len(a)-1
    sum=0
    while l<r:
        sum=sum+a[r]-a[l]
        l=l+1
        r=r-1
    return sum
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))