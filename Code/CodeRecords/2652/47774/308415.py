n,c,tot=map(int,input().split(' '))
a=[[0 for i in range(2)] for i in range(c+1)]
f=[0 for i in range(c+1)]
g=[0 for i in range(c+1)]
q=[]
for i in range(1,c+1):
    a[i][0],a[i][1]=map(int,input().split(' '))
a=sorted(a,key=(lambda x:x[0]))
sum=0
for i in range(1,int(n/2)+1):
    q.append(a[i][1])
    sum+=a[i][1]
for i in range(int(n/2)+1,c-int(n/2)):
    f[i]=sum
    q=sorted(q)
    if a[i][1]<q[-1]:
        sum-=q[0]
        sum+=a[i][1]
        q.remove(q[-1])
        q.append(a[i][1])
while len(q)!=0:
    q=sorted(q)
    q.remove(q[-1])
sum=0
for i in range(c,int(c-n/2),-1):
    q.append(a[i][1])
    sum+=a[i][1]
for i in range(c-int(n/2),int(n/2),-1):
    g[i]=sum
    q=sorted(q)
    if a[i][1]<q[-1]:
        sum-=q[0]
        sum+=a[i][1]
        q.remove(q[-1])
        q.append(a[i][1])
for i in range(c-int(n/2),int(n/2),-1):
    if f[i]+g[i]+a[i][1]<=tot:
        print(a[i][0])
    
    
