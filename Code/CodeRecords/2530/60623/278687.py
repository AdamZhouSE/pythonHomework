a=list(input())
b=list(input())
d={}
for i in a:
	d[i]=0
s=""
for i in b:
	if i not in d.keys():
		s+=i
	else:
		d[i]+=1
for key,value in d.items():
	s+=key*value
print(s)
