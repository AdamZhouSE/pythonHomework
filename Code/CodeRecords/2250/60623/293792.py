from collections import Counter
size=eval(input())
points=[]
for i in range(size):
	tempList=input().split(',')
	tL=[]
	for var in tempList:
		tL.append(int(var))
	points.append(tL)
print(max(sum(1 for j in points if j == i) + Counter([float('Inf') if i[1] - j[1] == 0 else (i[0] - j[0]) / (i[1] - j[1]) for j in points if j != i]).most_common(1)[0][1] if sum(1 for j in points if j == i) != len(points) else sum(1 for j in points if j == i) for i in points) if len(points) > 2 else len(points))