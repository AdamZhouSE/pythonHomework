n=int(input())
a=list(map(int,input().split()))
m=a[0]
d=1
for i in range(9):
	if a[i]<=m:
		m=a[i]
		d=i+1
if m>n:
	print(-1)
	exit()
ans=list(str(d)*(n//m))
rem=n-m*(n//m)
for i in range(len(ans)):
	if rem<=0:
		break
	for j in range(8,d-1,-1):
		if a[j]-a[d-1]<=rem:
			ans[i]=str(j+1)
			rem-=a[j]-a[d-1]
			break

print(''.join(ans))