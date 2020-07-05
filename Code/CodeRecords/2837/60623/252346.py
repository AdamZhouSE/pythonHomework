# Mislove 丢失了一个有 n 个正整数的数组，他只记得这个数组的一些规则：
# 数组中不同数字的数目不少于 l 个也不大于 r 个；
# 数组中每个元素要么为 1，要么是偶数且它的一半也在数组中。
# 例如，如果这个数组 n =5，l = 2, r = 3，那么这个数组可能为 [1, 2, 2, 4, 4] 或者 [1, 1, 1, 1, 2]，但是不可能为 [1, 2, 2, 3, 4] 因为 3 是奇数且不等于 1，
# 也不可能为 [1, 1, 2, 2, 16]，因为 16 的一半 8 不在数组中。
# Mislove 现在只记得 n,l 和 r，请你帮助他计算这个数组中所有元素的和的最小值和最大值。
temp=input().split()
num=int(temp[0])
l=int(temp[1])
r=int(temp[2])
if num==1:
	print("1 1")
else:
	min=0
	temp=1
	i=0
	minList=[]
	while i<l:
		minList.append(temp)
		temp *= 2
		i+=1
	for var in minList:
		min+=var
	min+=num-l
	max=0
	temp=1
	i=0
	maxList=[]
	while i<r:
		maxList.append(temp)
		temp *= 2
		i+=1
	for var in maxList:
		max+=var
	max+=(num-r)*maxList[len(maxList)-1]
	print(str(min)+" "+str(max))