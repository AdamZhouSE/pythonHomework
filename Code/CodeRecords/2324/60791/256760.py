a = [int(i) for i in input().split(',')]
k = int(input())
m = len(a)-1
while( m >= 0):
	for n in range(m):
		if(a[n] > a[n+1]):
			temp = a[n+1]
			a[n+1] = a[n]
			a[n] = temp
	m -=1
if(k>=(a[len(a)-1]-a[0])):
	print(a[len(a)-1]-a[0])
else:
	mi = a[0]+k
	ma = a[len(a)-1]-k
	if(mi > ma):
		temp = ma
		ma = mi 
		mi = temp
	for item in a:
		if(item+k>ma and item-k<mi):
			up = item+k-ma
			down = mi+k-item
			if(up>down):
				mi = item - k
			else:
				ma = item + k
print(ma-mi)