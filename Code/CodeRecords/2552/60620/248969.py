n,m=map(int,input().split())
a=[0 for i in range(n)]
num=0
for i in range(m):
    Q,L,R=map(int,input().split())
    if(Q==1):
        num+=1
        a[L-1]=num
        a[R-1]=num
    if(Q==2):
        b=[]
        for j in range(L-1,R):
            b.append(a[j])
        if(max(b)==0):print(4)
        else:print(max(b))