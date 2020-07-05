n,m,d=map(int,input().split())
a=[]
s=set()
for i in range(n):
	a+=list(map(int,input().split()))
a.sort()
mid=a[len(a)//2]
ans=0
for i in a:
	x=abs(i-mid)
	if x%d!=0:
		print(-1)
		exit()
	ans+=x//d
print(ans)