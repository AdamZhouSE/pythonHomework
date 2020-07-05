# 一个 n × n 的矩阵 a 是这样定义的:
# 第一行和第一列包含： a[i][1] = a[1][i]=1 对于所有的 i = 1, 2, ..., n.
# 表中剩余的每个数字等于它上面的数字和它的左边的数字的总和。换句话说，其余元素由公式 a[i][j] = a[i-1][j] + a[i][j-1] 定义
# 这些条件定义表中的所有值。
# 给你一个数 n，你需要求出给定的 n × n 的矩阵中最大的数
size=int(input())
if size==1:
	print(1)
else:
	l=[]
	i=0
	while i<size:
		temp=[]
		j=0
		while j<size:
			temp.append(1)
			j+=1
		i+=1
		l.append(temp)
	i=1
	print(l)
	while i<size:
		j=1
		while j<size:
			l[i][j]=l[i-1][j]+l[i][j-1]
			j+=1
		i+=1
	print(l[size-1][size-1])