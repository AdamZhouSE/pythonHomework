import math
def perm(n,m):
    return math.factorial(n)//math.factorial(n-m) 
n=int(input())
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range(n):
    x[i],y[i]=map(int,input().split())
x.sort()
y.sort()
pr=x[0]
cnt=0
nd=[0 for i in range(n)]
nd[0]=1
ans=0
for i in range(1,n):
    if(pr!=x[i]):
        pr=x[i]
        cnt+=1
    nd[cnt]+=1
for i in nd:
    if(i==0):
        break
    elif(i==1):
        continue
    else:
        ans+=perm(i,2)
pr=y[0]
cnt=0
nd=[0 for i in range(n)]
nd[0]=1
for i in range(1,n):
    if(pr!=y[i]):
        pr=y[i]
        cnt+=1
    nd[cnt]+=1
for i in nd:
    if(i==0):
        break
    elif(i==1):
        continue
    else:
        ans+=perm(i,2)
print(ans)
