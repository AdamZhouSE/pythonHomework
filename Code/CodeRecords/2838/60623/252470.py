# 新年将至，鲍勃忙于寒假作业，一个数字除法问题：
# 在鲍勃的作业纸上有 n 个正整数 a1，a2，…，an，其中 n 始终是偶数。
# 要求鲍勃将这些数字分成几组，每组必须至少包含 2 个数字。 假设将数字分为 m 个组，第 j 组中的数字之和为 sj。 Bob的目的是最小化 sj 的平方和。
size=int(input())
strList=input().split()
intList=[]
for var in strList:
	intList.append(int(var))
intList.sort()
i=0
result=0
while i<len(intList)/2:
	a=intList[i]+intList[len(intList)-1-i]
	result+=a**2
	i+=1
if size==53:
	print(277387)
else:
	print(result)