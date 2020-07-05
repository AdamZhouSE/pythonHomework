num = int(input())
a = [int(i) for i in input().split()]
count = len(a)
m = len(a)-1
while( m >= 0):
	for n in range(m):
		if(a[n] < a[n+1]):
			temp = a[n+1]
			a[n+1] = a[n]
			a[n] = temp
	m -=1
result = 0
for i in range(int(num/2)):
	result += (a[i]+a[num-1-i])**2
print(result)
