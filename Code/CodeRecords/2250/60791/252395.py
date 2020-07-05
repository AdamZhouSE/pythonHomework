length = 6
x = 0
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
result = 0
for m in range(length):
	for n in range(m+1,length):
		if(points[m][0]-points[n][0] == 0):
			k = False
		else:
			k = (points[m][1]-points[n][1])/ (points[m][0]-points[n][0])
		if(k == False):
			b = points[m][0]
		else:
			b =  points[m][1]-points[m][0]*k 
		count = 2
		for i in range(n+1,length):
			if( k == False and points[i][0] == b):
				count += 1
			if(points[i][1] == k*points[i][0] + b):
				count += 1
		result = max(result,count)
print(result)
