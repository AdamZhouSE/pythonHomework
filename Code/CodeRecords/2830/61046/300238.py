inn=input().split()
b=int(inn[0])
k=int(inn[1])
n=input().split()
n=list(map(int,n))
klist=[]
for i in range(1,k+1):
    klist.append(b**(k-i))
ans=0
for i in range(len(n)):
    ans+=n[i]*klist[i]
if ans%2!=0:
    print("odd")
else:
    print("even")