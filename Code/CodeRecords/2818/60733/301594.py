n,x=input().split()
n=int(n)
x=int(x)
c=list(map(int,input().split()))
c.sort()
d=0
for t in c:
	d=d+t*x
	if x>1: x-=1
print(d)