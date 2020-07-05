n,t = [int(i) for i in input().split()]
a =[int(i) for i in input().split()]
left = 0
right = 0
maxium = 0
for left in range(n):
	count = 0
	free = t
	for i in range(left,n):
		if(a[i] <= free):
			count += 1
			free -= a[i]
		else:
			break
	maxium = max(count,maxium)
print(maxium)