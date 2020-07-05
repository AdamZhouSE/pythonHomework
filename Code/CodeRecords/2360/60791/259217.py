
import itertools
import math
a = [int(i) for i in input().split(',')]
count = 0
for p in itertools.permutations(a):
	temp = True
	for i in range(len(p)-1):
		if(math.sqrt(p[i] + p[i+1])%1==0.0):
			pass
		else:
			temp = False
			break
	if(temp):
		count+=1
print(count)