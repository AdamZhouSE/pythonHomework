# 现在有一组 n 个数 a1, a2, ..., an，每一步你可以选择一个数加上或减去 1。现在想要让 a⋅a2⋅...⋅an=1 即这些数的乘积为 1，请问至少需要多少步？
size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
d={}
for var in intList:
	if var in d.keys():
		d[var]+=1
	else:
		d[var]=1
l=sorted(d.keys())
realD={}
for i in l:
	realD[i]=d[i]
resultD={}
resultD[1]=0
resultD[-1]=0
result=0
for key,values in realD.items():
	temp=key
	tem=0
	while abs(temp)!=1:
		if temp<=0:
			temp+=1
			tem+=1
		elif temp>0:
			temp-=1
			tem+=1
	result+=tem*values
	if temp==1:
		resultD[1]+=values
	else:
		resultD[-1]+=values
signal=1
for key,values in resultD.items():
	signal*=(key**values)
if signal==1:
	print(result)
else:
	print(result+2)