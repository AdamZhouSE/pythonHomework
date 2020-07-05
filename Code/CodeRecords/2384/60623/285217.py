size=int(input())
for i in range(size):
	a=input()
	tL=input().split()
	l=[]
	for var in tL:
		if int(var)>0:
			l.append(int(var))
	k=1
	while k in l:
		k+=1
	print(k)