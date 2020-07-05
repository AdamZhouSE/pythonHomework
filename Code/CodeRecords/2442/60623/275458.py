# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。
temp=input()[1:-1]
tempList=temp.split(',')
intList=[]
for i in tempList:
	intList.append(int(i))
intList.sort()
result=0
if len(intList)<2:
	print(0)
else:
	j=0
	while j<len(intList):
		if j==len(intList)-1:
			break
		if intList[j+1]-intList[j]>result:
			result=intList[j+1]-intList[j]
		j+=1
	print(result)