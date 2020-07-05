size=int(input())
for i in range(size):
	num=input()
	tL=input().split()
	l=[]
	for var in tL:
		l.append(int(var))
	d={}
	for var in l:
		if var not in d.keys():
			d[var]=1
		else:
			d[var]+=1
	t = sorted(d.items(), key=lambda item: item[1], reverse=True)
	# print(t)
	s=""
	k=0
	hhh=[]
	hhh.append(t[0][0])
	while k<len(t):
		if k==len(t)-1:
			hh = sorted(hhh)
			for var in hh:
				qq = 0
				while qq < d[var]:
					s += str(var) + " "
					qq += 1
			break
		if t[k][1]==t[k+1][1]:
			hhh.append(t[k+1][0])
		else:
			hh=sorted(hhh)
			for var in hh:
				qq=0
				while qq<d[var]:
					s+=str(var)+" "
					qq+=1
			hhh=[]
			hhh.append(t[k+1][0])
		k+=1
	print(s)