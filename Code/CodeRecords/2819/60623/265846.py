# 学校有 n 个小组外出游玩，第 i 个小组有 si (1 ≤ si ≤ 4) 个人，同学们想要打出租，每辆车最多坐4个人，同个小组必须坐在同一辆车上，
# 求最少需要多少辆车才能让同学们都坐上出租车
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
result=0
resultD={}
resultD[1]=0
resultD[2]=0
resultD[3]=0
for key,value in realD.items():
	if key==4:
		result+=value
	if key==2:
		result+=value//2
		resultD[2]=value%2
	if key==3 or key==1:
		resultD[key]=value
result+=resultD[3]
resultD[1]=resultD[1]-resultD[3]
if resultD[1]<=0:
	if resultD[2]==1:
		result+=1
else:
	if resultD[2]==1:
		resultD[1]-=2
		result+=1
	if resultD[1]>0:
		result+=(resultD[1]//4)+1
print(result)