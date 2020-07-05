num = 4
a= eval(input())
count = len(a)
m = len(a)-1
while( m >= 0):
	for n in range(m):
		if(a[n] > a[n+1]):
			temp = a[n+1]
			a[n+1] = a[n]
			a[n] = temp
	m -=1
print(a)