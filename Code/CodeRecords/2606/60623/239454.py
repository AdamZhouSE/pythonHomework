# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
a=input()[1:-1]
target=int(input())
l=a.split(',')
i=0
isExist=False
while i<len(a):
	if int(l[i])==target:
		print(i)
		isExist=True
		break
	i=i+1
if isExist==False:
	print(-1)
