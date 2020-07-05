import math
size=int(input())
for i in range(size):
	a=input()
	t1=input().split()
	l1=[]
	for var in t1:
		l1.append(int(var))
	t2 = input().split()
	l2 = []
	for var in t2:
		l2.append(int(var))
	result=0
	for var1 in l1:
		for var2 in l2:
			if pow(var1,var2)>pow(var2,var1):
				result+=1
	print(result)