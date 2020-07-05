n=int(input())
a=[]
b=[]
for i in range(n):
	x,y=map(int,input().split())
	a.append(x)
	b.append(y)
ans=[0]*n
ans[0]=-1
ans[-1]=1
for i in range(1,n-1):
	if ans[i-1]!=1 and a[i]-b[i]>a[i-1]:
		ans[i]=-1
	elif ans[i-1]==1 and a[i]-b[i]>a[i-1]+b[i-1]:
		ans[i]=-1
	elif a[i]+b[i]<a[i+1]:
		ans[i]=1
print (sum([1 for i in ans if i!=0]))
#print (ans)
