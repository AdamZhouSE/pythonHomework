# 桌面上水平放置着 n 张卡片，每张卡片在 xi 位置上，不同卡片可能在同一位置上，现规定：
# 把卡片往左或右移动两个单位不需要费用
# 往左或右移动一个单位则需要花费一个硬币
# 现在要将所有卡片都移动到同一个位置上（可以是任意位置），求最少的硬币消耗。
tempList=input().split(',')
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
resultD[0]=0
resultD[1]=0
for i in l:
	if i%2==0:
		resultD[0]+=realD[i]
	else:
		resultD[1]+=realD[i]
if resultD[0]>=resultD[1]:
	print(resultD[1])
else:
	print(resultD[0])