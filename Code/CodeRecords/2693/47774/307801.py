st=str(input())
l=len(st)
n,m=0,0
Mod = 998244353
c=[[0 for i in range(110)] for i in range(110)]
f=[[0 for i in range(110)] for i in range(110)]
A=[0 for i in range(110)]
pw=[0 for i in range(110)]
for i in range(l):
    if st[i]=='0':
        n+=1
    else:
        m+=1
N=n+m
c[0][0]=1
for i in range(1,N+1):
    c[i][0]=1
    for j in range(1,N+1):
        c[i][j]=(c[i-1][j-1]+c[i-1][j])%Mod
A[0]=1
pw[0]=1
f[0][0]=1
for i in range(1,N+1):
    A[i]=A[i-1]*(i%Mod)
for i in range(1,N+1):
    pw[i]=pw[i-1]*(N%Mod)
for i in range(1,n+1):
    for j in range(m+1):
        for k in range(1,i+1,2):
            for l in range(j+1):
                kl=k+l
                f[i][j]-=A[kl-1]*c[i-1][k-1]%Mod*c[j][l]%Mod*f[i-k][j-l]%Mod
                f[i][j]%=Mod
                
ans=0
for i in range(n+1):
    for j in range(m+1):
        ans+=f[i][j]*c[n][i]%Mod*c[m][j]%Mod*pw[N-i-j]%Mod
        ans%=Mod
if ans<0:
    ans+=Mod
print(ans)
                
                
                
                