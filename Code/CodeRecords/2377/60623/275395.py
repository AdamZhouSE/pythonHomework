# 回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。
# 给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。
size=int(input())
l=[]
for i in range(size):
	temp=input().split(',')
	l.append(temp)
aX=int(l[0][0])
aY=int(l[0][1])
bX=int(l[1][0])
bY=int(l[1][1])
cX=int(l[2][0])
cY=int(l[2][1])
k1=(bY-aY)/(bX-aX)
k2=(cY-aY)/(cX-aX)
if k1==k2:
	print("False")
else:
	print("True")