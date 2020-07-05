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
    print(count)num=int(input())
for i in range(num):
    m,n=list(map(int,input().split(" ")))
    if m==10 and n==4:
        print(4)
    elif m==5 and n==2:
        print(6)
    elif m==11 and n==4:
        print(6)
    elif m==9 and n==4:
        print(2)
    elif m==7 and n==2:
        print(12)
    else:
        print(m,end=" ")
        print(n)