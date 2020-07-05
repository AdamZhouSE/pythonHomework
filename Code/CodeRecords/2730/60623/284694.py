import math
num=int(input())
for i in range(num):
	size=int(input())
	tempL=input().split()
	intL=[]
	for var in tempL:
		intL.append(int(var))
	signal=0
	for var in intL:
		if var%3==0:
			signal=1
			print(1)
			break
	if signal==0:
		t=0
		for var in intL:
			if ((t+var)%3)==0:
				signal=1
				print(1)
				break
			else:
				t+=var
	if signal==0:
		t=0
		for var in intL:
			if abs(t-var)%3==0:
				signal=1
				print(1)
				break
			else:
				t=abs(t-var)
	if signal==0:
		print(0)
