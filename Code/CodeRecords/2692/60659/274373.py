import re
list=input()
pattern=re.compile("\d+")
weight=pattern.findall(list)
sum=0
for i in range(len(weight)):
	weight[i]=int(weight[i])
	sum+=weight[i]
D=int(input())

max=max(weight)
if sum//D>max:
	res=sum//D
else:
	res=max
while(True):
	d=1
	temp=0
	for i in weight:
		if temp+i<=res:
			temp+=i
		else:
			temp=i
			d+=1
	if(d<=D):
		break
	else:
		res+=1
print(res)