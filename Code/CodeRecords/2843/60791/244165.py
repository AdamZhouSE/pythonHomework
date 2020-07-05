n = int(input())
a = [int(i) for i in input().split()]
b = []
for i in range(n-1):
    b.append(a[i] + a[i+1])
b.append(a[n-1])
for i in range((len(b)-1)):
	print(b[i],end=' ')
print(b[n-1])
