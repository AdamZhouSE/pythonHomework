n=int(input())
a=list()
i=0
while i<n:
	str=list(map(int,input().split(" ")))
	a.append(str)
	i=i+1

i=0
while i<n:
	print(pow(a[i][1],a[i][0]-1))
	i=i+1