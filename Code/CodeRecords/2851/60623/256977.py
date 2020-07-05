# 平面上有 n 个点，你需要以 x 轴和 y 轴为两条边，做一个最小的等腰直角三角形以覆盖所有的点，请问这个三角形的最短边是多少？
size=int(input())
tempList=[]
resultList=[]
for i in range(size):
	tempList=input().split()
	resultList.append(int(tempList[0])+int(tempList[1]))
resultList.sort()
print(resultList[len(resultList)-1])