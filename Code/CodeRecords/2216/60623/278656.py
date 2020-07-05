sign=[]
z=[]
m=[]
s=input()
i=0
if s[0].isdigit():
	s='+'+s
while i<len(s):
	if s[i]=='+' or s[i]=='-':
		sign.append(s[i])
	elif (s[i-1]=='+' or s[i-1]=='-') and s[i].isdigit():
		if s[i+1].isdigit():
			z.append(int(s[i]+s[i+1]))
			i+=1
		else:
			z.append(int(s[i]))
	elif (s[i-1]=='/') and s[i].isdigit():
		if i==len(s)-1:
			m.append(int(s[i]))
			break
		if s[i+1].isdigit():
			m.append(int(s[i] + s[i + 1]))
			i += 1
		else:
			m.append(int(s[i]))
	i+=1
mm=1
for i in m:
	mm*=i
j=0
result=0
while j<len(z):
	if sign[j]=='+':
		result+=z[j]*(mm/m[j])
	else:
		result-=z[j]*(mm/m[j])
	j+=1
a=int(result)
b=mm
while b:
	a,b=b,a%b

print(str(int(result)//a)+"/"+str(mm//a))