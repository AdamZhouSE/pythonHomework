# 给你一个由 n 个不同整数组成的序列 a。您可以将这个序列分成两个序列 b 和 c，这样每个元素都正好属于其中一个序列。
# 设 B 是属于 b 的元素之和，C 是属于 c 的元素之和（如果其中一些序列为空，则其和为0）。B - C 的最大可能值是多少？
size=int(input())
strList=input().split()
intList=[]
for var in strList:
	intList.append(int(var))
i=0
resultList=[]
while i<size-1:
	j=0
	aAll=0
	while j<i+1:
		aAll=aAll+intList[j]
		j+=1
	k=size-1
	bAll=0
	while k>=i+1:
		bAll=bAll+intList[k]
		k-=1
	result=aAll-bAll
	resultList.append(result)
	i+=1
result=0
for val in intList:
	result+=val
resultList.append(abs(result))
resultList.sort()
print(resultList[len(resultList)-1])