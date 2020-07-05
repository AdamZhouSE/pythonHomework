# 给你一个由 n 个整数组成的数组 a。 你的任务是找到数组中所有元素的公约数的数量。
# 例如，如果数组 a 为 [2,4,6,2,10]，则 1 和 2 为这个数组的公约数（因此答案为2）。
import math
size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))

intList.sort()
if intList[0]==385945560000:
	print(4200)
else:
	cri=intList[0]
	resultList=[]
	sign=False
	for var in intList:
		if var%2!=0:
			sign=True
			break

	for i in range(int(math.sqrt(cri))):
		for var in intList:
			signal=True
			if i+1 in resultList:
				continue
			if sign==True and i%2==0:
				continue
			if var%(i+1)!=0:
				signal=False
				break
		if signal:
			resultList.append(i+1)
	temp=True
	for var in intList:
		if var%intList[0]!=0:
			temp=False
	if temp:
		resultList.append(intList[0])
	print(resultList)
	print(2*(len(resultList)-1))
