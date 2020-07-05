# 你现在拿到一个由 24 个 0 和 1 个 1 组成的 5*5 的矩阵。现在你需要把这个 1 移动到矩阵的中心点，使得这个矩阵变得 “优雅”，只能上下左右一格一格移动，请你输出最小移动数。
l=[]
for i in range(5):
	temp=input().split()
	l.append(temp)
a=0
row=0
column=0
while a<5:
	b = 0
	while b<5:
		if l[a][b]=='1':
			row=a
			column=b
		b+=1
	a+=1
print(abs(2-row)+abs(2-column))