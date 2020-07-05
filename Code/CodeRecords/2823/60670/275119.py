n,k=map(int,input().split())
f=[[0 for i in range(0,k+1)] for i in range(0,n+1)]
f[1][0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        for t in range(1,int(i**0.5)):
            if i%t==0:
                f[i][j]=(f[i][j]+f[t][j-1])%1000000007
                if i//t!=i:
                    f[i][j]=(f[i][j]+f[i//t][j-1])%1000000007
answer=0
for i in range(1,n+1):
    answer=(answer+f[i][k])%1000000007
print(answer)