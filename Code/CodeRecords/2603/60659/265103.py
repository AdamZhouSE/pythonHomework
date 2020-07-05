import re
list=input()
pattern=re.compile(r'\d+')
num=pattern.findall(list)
for i in range(len(num)):
	num[i]=int(num[i])
k=int(input())
result=[]
for i in range(len(num)):
	for j in range(i+1,len(num)):
		if num[i]-num[j]>=0:
			result.append(num[i]-num[j])
		else:
			result.append(num[j]-num[i])
result.sort()
print(result[k-1])