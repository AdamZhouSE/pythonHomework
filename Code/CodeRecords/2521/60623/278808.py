l=eval(input())
d={}
for i in l:
	if i not in d.keys():
		d[i]=1
	else:
		d[i]+=1
s=""
while len(s)<len(l):
	for key,value in d.items():
		if value!=0:
			s+=str(key)
			value-=1
print(s)