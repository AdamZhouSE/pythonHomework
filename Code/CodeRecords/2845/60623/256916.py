# 一天，Dima 和 Alex 就笔记本电脑的价格和质量发生了争执。迪玛认为笔记本电脑越贵越好，Alex 不同意。
# Alex 认为存在价格更低，但质量更好（价格严格小于且质量严格大于）的笔记本。
# 我们为您介绍了 n 台笔记本电脑。请问这些笔记本电脑中是否存在支持 Alex 观点的一台。
size=int(input())
priceList=[]
quantityList=[]
for i in range(size):
	tempList=input().split()
	priceList.append(int(tempList[0]))
	quantityList.append(int(tempList[1]))
i=0
while i<size:
	if i==size-1:
		break
	else:
		if priceList[i]<priceList[i+1] and quantityList[i]>quantityList[i+1]:
			print("Happy Alex")
		i+=1
if i==size-1:
	print("Poor Alex")