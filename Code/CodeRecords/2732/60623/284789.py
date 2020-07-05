import math
size=int(input())
for i in range(size):
	tL=input().split()
	l=[]
	for var in tL:
		l.append(int(var))
	print(math.pow(l[0],l[1])%l[2])