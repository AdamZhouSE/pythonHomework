i=int(input())
a=list()
j=0
while j<i:
	a.append(int(input()))
	j=j+1

j=0
while j<i:
	print(a[j]*(2*a[j]+1))
	j=j+1