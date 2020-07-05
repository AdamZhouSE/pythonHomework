# 有一天，史派克感兴趣于如何以非降序对整数 a1，a2，...，an 进行排序。 他唯一可以执行的操作是 shift。 也就是说，她可以将序列的最后一个元素移到其开头：
# a1，a2，...，an → an，a1，a2，...，an-1。
# 帮助史派克计算：对序列进行非降序排序所需的最少操作数是多少？
def isHigh(l):
	size=len(l)
	if size==1:
		return True
	else:
		i=0
		while i<len(l)-1:
			if l[i]<=l[i+1]:
				i+=1
				continue
			else:
				return False
		return True



size=int(input())
strList=input().split()
intList=[]
for var in strList:
	intList.append(int(var))
i=0
result=0
signal=False
while i<size:
	if not isHigh(intList):
		temp=intList[len(intList)-1]
		del intList[len(intList)-1]
		intList.insert(0,temp)
		result+=1
		i+=1
		continue
	else:
		signal=True
		break
if signal:
	print(result)
else:
	print(-1)