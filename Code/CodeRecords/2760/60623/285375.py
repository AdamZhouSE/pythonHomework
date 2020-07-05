size=int(input())
for i in range(size):
	tL=input().split()
	num=int(tL[0])
	money=int(tL[1])
	l=[]
	for var in range(num):
		l.append(money)
	result=[0,0]
	j=0
	while j<len(l):
		if j%2==0:
			result[0]+=l[j]
		else:
			result[1]+=l[j]
		j+=1
	t=sorted(result)
	print(t[len(t)-1])