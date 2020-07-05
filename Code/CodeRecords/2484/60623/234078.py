# 给定两个分别为大小N和M的数组A和B。任务是在这两个数组之间找到并集。 可以将两个数组的并集定义为包含两个数组中不同元素的集合。如果存在重复，则只应合并打印一次元素。
size=int(input())
a=0
while a<size:
	b=input()#用不到
	str1=input().split()
	str2=input().split()
	i=0
	while i<len(str1):
		if(str1[i] not in str2):
			str2.append(str1[i])
		i=i+1
	print(len(str2))
	a=a+1