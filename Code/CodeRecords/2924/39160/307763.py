n,r,avg = map(int,input().split())
x = []
s = 0
for i in range(n):
	a,b = map(int,input().split())
	s += a
	x.append((a,b))
rem = avg*n - s
x.sort(key=lambda i: i[1])
i = 0
count = 0
while rem>0:
	if x[i][0] < r:
		v = min(rem, r - x[i][0])
		count += v*x[i][1]
		rem -= v
	i+=1
print(count)