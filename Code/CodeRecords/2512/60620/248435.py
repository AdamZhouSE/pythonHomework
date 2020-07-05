N,P=map(int,input().split())
a=list(map(int,input().split()))
M=int(input())
for i in range(M):
    s=input().split()
    if(s[0]=='1'):
        t=int(s[1])
        g=int(s[2])
        c=int(s[3])
        for j in range(1,N+1):
            if(j>=t and j<=g):
                a[j-1]=a[j-1]*c
    if(s[0]=='2'):
        t=int(s[1])
        g=int(s[2])
        c=int(s[3])
        for j in range(1,N+1):
            if(j>=t and j<=g):
                a[j-1]=a[j-1]+c
    if(s[0]=='3'):
        t=int(s[1])
        g=int(s[2])
        b=[]
        for j in range(1,N+1):
            if(j>=t and j<=g):
                b.append(a[j-1])
        result=sum(b)%P
        print(result)
            