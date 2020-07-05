from collections import defaultdict

f=defaultdict(int)
q=[0]*300000
top=0
nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
now=0
x=0
ans=0
c=''
for i in range(n):
    move=input().split(' ')
    x=int(move[0])
    c=move[1]
    if c=='R':
        top+=1
        q[top]=now
        f[q[top]]+=1
        top+=1
        q[top]=now+x
        f[q[top]]-=1
        now+=x
    else:
        top+=1
        q[top]=now-x
        f[q[top]]+=1
        top+=1
        q[top]=now
        f[q[top]]-=1
        now-=x
q2=q[1:top+1]
q2.sort()
q2.extend(q[top+1:])
q2.insert(0,q[0])
q=q2
now=f[q[1]]
for i in range(2,top+1):
    if q[i]!=q[i-1]:
        if now>=m:
            ans+=q[i]-q[i-1]
        now+=f[q[i]]
print(ans,end='')