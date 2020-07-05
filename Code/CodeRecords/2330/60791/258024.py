import math

def distance(dot1,dot2):
	return math.sqrt((dot2[1]-dot1[1])**2 +(dot2[0]-dot1[0])**2)
	
def mid(dot1,dot2):
	return [(dot1[0]+dot2[0])/2,(dot1[1]+dot2[1])/2]
	
def compute_area(a,b):
	return a*b
	
n = int(input())
points = []
x = 0
while(x<n):
    temp = [int(i) for i in input().split(',')]
    points.append(temp)
    x+=1
pair = []
dis = []
for x in range(n):
	for y in range(x+1,n):
		temp = []
		dis.append(distance(points[x],points[y]))
		temp.append(points[x])
		temp.append(points[y])
		temp.append(mid(points[x],points[y]))
		pair.append(temp)
m = len(dis)-1
while( m >= 0):
	for i in range(m):
		if(dis[i] < dis[i+1]):
			temp = dis[i+1]
			dis[i+1] = dis[i]
			dis[i] = temp
			temp1 = pair[i+1]
			pair[i+1] = pair[i]
			pair[i] = temp1
	m -=1
area = 0
for i in range(len(dis)-1):
	if(dis[i] == dis[i+1]):
		r = i+1
		for x in range(i+1,len(dis)-1):
			if(dis[i] == dis[x]):
				r = x
			else:
				break
		for x in range(i+1,x+1):
			if(pair[i][2] == pair[x][2]):
				temp = compute_area(distance(pair[i][0],pair[x][0]),distance(pair[i][0],pair[x][1]))
				if(area == 0):
					area = temp
				else:
					area = min(area,temp)
print('%.4f'%area)