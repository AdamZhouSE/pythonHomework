T=int(input())
for  i in range(T):
	line=input().split(" ")
	num=input().split(" ")
	n=int(line[0])
	m=int(line[1])
	l=int(line[2])
	r=int(line[3])
	for j in range(n):
		num[j]=int(num[j])
	counter=1
	for j in range(n+m):
		counter*=j+1
	for j in range(r-l):
		num.append(j+l)
	while r-l<m:
		num.append(r)
		m-=1
	type = []
	number=[]
	for x in num:
		if not (x in type):
			type.append(x)
			number.append(1)
		else:
			number[type.index(x)] += 1
	counts = 1
	for j in number:
		sum=1
		for x in range(1,j+1):
			sum*=x
		counts*=sum
	print((counter//counts)%998244353)