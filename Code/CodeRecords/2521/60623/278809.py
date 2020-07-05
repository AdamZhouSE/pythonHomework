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
print("[",end='')
k=0
while k<len(s):
	if k==len(s)-1:
		print(s[k],end=']')
	else:
		print(s[k],end=',')