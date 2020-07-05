import collections
h=int(input())
points=[]
for i in range(h):
	templist=input()[1:-1].split(',')
	t=[]
	for var in templist:
		t.append(round(float(var)))
	points.append(t)
print(points)