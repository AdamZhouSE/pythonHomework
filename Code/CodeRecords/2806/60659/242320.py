n=int(input())
price=0
counter=0
for i in range(n):
	l=input().split()
	a=int(l[0])
	p=int(l[1])
	if p<price:
		price=p
	elif price==0:
		price=p
	counter+=price*a
print(counter)