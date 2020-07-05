list1=list(map(int,input().strip().split(' ')))
n=list1[0]
m=list1[1]
s=[0]
for i in range(n):
    s.append(int(input()))
a=[(0,0)]
for j in range(m):
    list1 = list(map(int, input().strip().split(' ')))
    a.append((list1[0],list1[1]))
a.sort()
for j in range(11000):
    a.append((0,0))
t=0
q=[]
sum=[]
ans=0
for j in range(110000):
    sum.append(0)
for i in range(1,n+1):
    while t+1<len(a) and a[t+1][0]<=i:
        t+=1
        q.append(a[t][1])
        q.sort()
        sum[a[t][1]]+=1
    while len(q)>(s[i]+ans):
        sum[q[0]]-=1
        q.pop()
    ans+=sum[i]
print(ans)