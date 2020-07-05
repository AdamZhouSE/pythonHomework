T = int(input())
while T > 0:
	T -= 1
	r = int(input())
	count = 0
	i, j= 1, 1
	while i**2 + j**2 <= (2*r)**2:
		while i**2 + j**2 <= (2*r)**2:
			count += 1
			j += 1
		i += 1
		j = 1
	print(count)