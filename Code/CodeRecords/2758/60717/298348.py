tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
if n<m:
    print(0)
else:
    a=1
    index=n-1
    while index!=0:
        a*=index
        index-=1
    b=1
    index=n-1
    tmp=m*n
    while index!=0:
        b*=tmp
        index-=1
        tmp-=1
    print(int(b/a/n)%10007)