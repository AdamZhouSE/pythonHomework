# 现在给定 n 个整数，请使用其中任意个整数（每个只能使用一次），得到一个最大的为偶数的和。
a=input()
b=input().split()
i=0
l=[]
oddL=[]
result=0
while i<len(b):
	l.append(int(b[i]))
	i+=1
for val in l:
	if val%2==0:
		result=result+val
	else:
		oddL.append(val)
if len(oddL)%2==0:
	for val in oddL:
		result=result+val;
else:
	oddL.sort()
	j=len(oddL)-1
	while j!=0:
		result=result+oddL[j]
		j-=1
print(result)