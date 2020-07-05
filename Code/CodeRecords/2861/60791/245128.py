num = int(input())
a = [int(i) for i in input().split()]

m = len(a)-1
while( m >= 0):
	for n in range(m):
		if(a[n] < a[n+1]):
			temp = a[n+1]
			a[n+1] = a[n]
			a[n] = temp
	m -=1
result = 0
n = 0
while(n < num):
	result += (a[n] - a[n-1])
	n+=2
print(result)