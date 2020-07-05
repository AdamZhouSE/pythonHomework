num=int(input())

def countnum(i,m,l):
    a=l[::]
    c=0
    if i==len(a)-1:
        return m-a[i]+1
    while a[i]*(2**(len(a)-1-i))<=m:
        c+=countnum(i+1,m,a)
        a[i]+=1
        for j in range(i+1,len(a)):
            a[j]=a[j-1]*2
    return c

for i in range(num):
    m,n=list(map(int,input().split(" ")))
    l=[0]*n
    count=0
    for j in range(n):
        l[j]=2**j
    count+=countnum(0,m,l)
    print(count)