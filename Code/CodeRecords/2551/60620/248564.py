N,M=map(int,input().split())
a=[0 for i in range(N)]
for i in range(M):
    inp=input().split()
    if(inp[0]=='0'):
        s=int(inp[1])
        e=int(inp[2])
        for j in range(s-1,e):
            if(a[j]==0):a[j]=1
            elif(a[j]==1):a[j]=0
    if(inp[0]=='1'):
        num=0
        s=int(inp[1])
        e=int(inp[2])
        for j in range(s-1,e):
            if(a[j]==1):num+=1
        print(num)
        
        