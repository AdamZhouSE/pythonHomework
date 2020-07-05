# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
size=int(input())
l=[]
for i in range(size):
	temp=input().split(',')
	l.append(temp)
if len(l)<=2:
	print("True")
else:
	aX=int(l[0][0])
	aY=int(l[0][1])
	bX=int(l[1][0])
	bY=int(l[1][1])
	k=(bY-aY)/(bX-aX)
	i=2
	while i<len(l):
		tempX=int(l[i][0])
		tempY=int(l[i][1])
		tem=(tempY-aY)/(tempX-aX)
		if tem!=k:
			print("False")
		i+=1
	if i==len(l)-1:
		print("True")
	