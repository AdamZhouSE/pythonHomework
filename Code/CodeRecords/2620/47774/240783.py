n=eval(input())
for i in range(n):
	d=eval(input())
	sum=0
	for j in range(1,d+1):
		sum+=j**5
	print(sum)