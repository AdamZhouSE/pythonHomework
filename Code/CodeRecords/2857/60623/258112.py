# 给你一个由 n 个整数组成的数组 a。 你的任务是找到数组中所有元素的公约数的数量。
# 例如，如果数组 a 为 [2,4,6,2,10]，则 1 和 2 为这个数组的公约数（因此答案为2）。
size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
intList.sort()
cri=intList[0]
resultList=[]
for i in range(cri):
	for var in intList:
		signal=True
		if var%(i+1)!=0:
			signal=False
			break
	if signal:
		resultList.append(i+1)
print(len(resultList))
