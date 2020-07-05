tl=input().split(',')
l=[]
for var in tl:
	l.append(int(var))
K=int(input())
L=sorted(l)
if len(L)==1:
	print(L)
else:
	resultList=[]
	gap=0
	while gap<len(L)-1:
		# tempList = []
		# for var in L:
		# 	tempList.append(var)
		# i=0
		# while i<=gap:
		# 	tempList[i]+=K
		# 	i+=1
		# while i<len(L):
		# 	tempList[i]-=K
		# 	i+=1
		big=0
		small=0
		if L[gap]+K>=L[len(L)-1]:
			big=L[gap]+K
		else:
			big=L[len(L)-1]
		if L[0]+K<=L[gap+1]-K:
			small=L[0]+K
		else:
			small=L[gap+1]-K
		resultList.append(big-small)
		gap+=1
	t=sorted(resultList)
	print(t[0])