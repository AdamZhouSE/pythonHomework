def find(num,binas,ss,M,K):
    a1=(2**K-1)&(num<<1)
    a2=a1+1
    if binas[a1]==0:
        binas[a1]=1
        ss.append(0)
        find(a1,binas,ss,M,K)
        return
    if binas[a2]==0:
        binas[a2]=1
        ss.append(1)
        find(a2,binas,ss,M,K)
        return

K=int(input())
M=2**K
binas=[]
for i in range(M):
    binas.append(0)
ss=[]
ini=2**(K-1)
ini_=2**(K-1)
binas[0]=1
for i in range(K-1):
    binas[ini]=1
    ini_/=2
    ini=ini+int(ini_)
find(0,binas,ss,M,K)
s=""
for i in range(K):s+="0"
for e in ss:s+=str(e)
print(M,s)