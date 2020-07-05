import math
def perm(n):
    return math.factorial(n)//math.factorial(n-2)//2
n=int(input())
x=[]
y=[]
s={}
for i in range(n):
    xx,yy=map(int,input().split())
    x.append(xx)
    y.append(yy)
    ss=str(xx)+','+str(yy)
    if(ss in s):
        s[ss]+=1
    else:
        s[ss]=1
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
        ans+=perm(i)
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
        ans+=perm(i)
dd=0
for i in list(s.values()):
    if(i>1):
        dd+=perm(i)
print(ans-dd)
