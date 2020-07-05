import math
def perm(n,m):
    return math.factorial(n)//math.factorial(n-m) 
n=int(input())
x=[]
y=[]
for i in range(n):
    xx,yy=map(int,input().split())
    if((xx not in x)or(yy not in y)):
        x.append(xx)
        y.append(yy)
x.sort()
y.sort()
pr=x[0]
cnt=0
nd=[0 for i in range(n)]
nd[0]=1
ans=0
for i in range(1,len(x)):
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
for i in range(1,len(y)):
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
print(int(ans/2))
