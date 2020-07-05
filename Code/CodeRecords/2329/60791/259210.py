from collections import Counter
import math
a = [int(i) for i in input().split(',')]
DSU = [0]*len(a)
mark = 0
for x in range(len(a)):
	if(DSU[x]==0):
		mark+=1
		DSU[x] = mark
	for y in range(len(a)):
		if(math.gcd(a[x],a[y])!=1 and DSU[y]==0 and x!=y):
			DSU[y] = DSU[x]
		elif(math.gcd(a[x],a[y])!=1 and DSU[y]!=0 and x!=y):
			DSU[x] = DSU[y]
dic = dict(Counter(DSU))
res = 0
for key,value in dic.items():
	res = max(res,value)
print(res)