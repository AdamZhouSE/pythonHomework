n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
l=[0]*(n+1)
for i in range(m):
	x,y=map(int,input().split())
	l[x]+=1
	if y<n:
		l[y+1]-=1

c=0
for i in range(n+1):
	c+=l[i]
	l[i]=c

l.sort(reverse=True)
a.sort(reverse=True)
 
ans=0
for i in range(n+1):
	ans+=l[i]*a[i]
print(ans)