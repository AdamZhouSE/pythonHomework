# Lahub 很无聊，所以他在纸上玩一个游戏：
# 在纸上写上 n 个数，只可能是 0 或者 1。他只允许做一次操作：对连续的 k 个数执行 x = 1 - x 的操作。
# 请问在执行这样一个操作后，纸上最多能有多少个 1。
def oneCount(l):
	result=0
	for i in l:
		if i==1:
			result+=1
	return result


size=int(input())
tempList=input().split()
intList=[]
for var in tempList:
	intList.append(int(var))
i=0
resultList=[]
while i<size:
	j=i
	while j<size:
		k=i
		#这样写的话，tempList和intList就是同一个，和所想不一样
		tempList = []
		for var in intList:
			tempList.append(var)
		while k<=j:
			tempList[k]=1-tempList[k]
			k+=1
		result=oneCount(tempList)
		resultList.append(result)
		j+=1
	i+=1
resultList.sort()
print(resultList[len(resultList)-1])