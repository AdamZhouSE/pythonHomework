t=int(input())
for ex in range(0,t):
    n,l,r=map(int,input().split(" "))
    b=[]
    while n>0:
        b.append(n%2)
        n=n//2
    for i in range(l-1,r):
        if b[i]==1:
            b[i]=0
        else:
            b[i]=1
    re=0
    for i in range(0,len(b)):
        re+=pow(2,i)*b[i]
    print(re)