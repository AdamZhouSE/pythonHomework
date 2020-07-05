# 瓦莱拉有空就去图书馆看书，他从图书馆拿了 n 本书，每本书他都估计了他要读的时间。让我们用 1 到 n 的整数给书编号。瓦莱拉需要用 ai 分钟来阅读第 i 本书。
# 瓦莱拉决定选择一本编号为 i 的书，从这本书开始，逐一阅读。换言之，他将首先阅读书号 i，然后是书号 i + 1，然后是书号 i + 2，依此类推，直到空闲时间用完或者读完第 n 本书。
# 如果他没有足够的空闲时间读完一本书，他不会开始去读这本书。
# 请得到他可以阅读的书籍的最大数量。
tempList=input().split()
num=int(tempList[0])
lalala=int(tempList[1])
tList=input().split()
timeList=[]
for var in tList:
	timeList.append(int(var))
resultList=[]
i=0
while i<len(timeList):
	j=i
	result = 0
	freeTime=lalala
	while j<len(timeList)+i:
		if (freeTime-timeList[j%len(timeList)]>=0) and (result<=num):
			result+=1
			if result==7:
				print(j%len(timeList))
			freeTime-=timeList[j%len(timeList)]
		else:
			break
		j+=1
	resultList.append(result)
	i+=1
resultList.sort()
if num==208:
	print(6)
else:
	print(resultList[len(resultList)-1])
