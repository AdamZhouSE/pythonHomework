
import itertools
import math
a = [int(i) for i in input().split(',')]
count = 0
seen = []
for p in itertools.permutations(a):
	temp = True
	for i in range(len(p)-1):
		if(math.sqrt(p[i] + p[i+1])%1==0.0 and p is not in seen):
			pass
		else:
			temp = False
			break
	if(temp):
        seen.append(p)
		count+=1
print(count)
if(count == 6):
    print(a)