import math

n = int(input())
a = [int(i) for i in input().split()]

mina = a[0]
result = True
for i in range(len(a)):
	if(mina > a[i]):
		mina = a[i]

for i in range(len(a)):
	if(a[i] % mina != 0):
		result = False
		break
if(mina == 1):
	print(1)
elif(result == False):
	ma = 0
	for m in range(int(math.sqrt(mina-1))):
		re = True
		for n in range(len(a)):
			if(a[n]% (m+1) != 0):
				re = False
				break
		if(re):
			ma = m+1
	mina = ma
	if(mina == 1):
		print(1)
	else:
		count = 1
		i=2
		target = mina 
		while(i<int(math.sqrt(target))):
			if(mina%i == 0):
				count+=1
			i+=1
		print(count*4)
else:
	count = 1
	i=2
	target = int(math.sqrt(mina)) 
	while(i<=target):
		if(mina%i == 0):
			count+=1
		i+=1
	print(2*count)
