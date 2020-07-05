N=int(input())
I=list(map(int,input().split()))
c=[]
A=[]
B=[]
for i in range(N-1):
    a,b=map(int,input().split())
    c.append([a,b])
    A.append(a)
    B.append(b)
s=0
for i in range(N):
    if(I[i]>=0):
        s+=I[i]
    if(I[i]<0 and (A.count(i+1)+B.count(i+1))>=2):
        s+=I[i]
print(s,end="")