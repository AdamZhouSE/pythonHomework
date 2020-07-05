R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())
visited = []
for x in range(R):
	temp = []
	for y in range(C):
		temp.append(False)
	visited.append(temp)
result = [[r0,c0]]
visited[r0][c0] = True
dis = 1
right = True
r = r0
c = c0
while(visited[0][0]!= True or visited[R-1][0]!=True or visited[0][C-1]!=True or visited[R-1][C-1]!=True):
	if(right):
		for i in range(1,dis+1):
			c = c+1
			if(r>=R or c >= C or c<0 or r<0):
				pass
			else:
				visited[r][c] = True
				result.append([r,c])
		for i in range(1,dis+1):
			r = r+1
			if(r>=R or c >= C or c<0 or r<0):
				pass
			else:
				visited[r][c] = True
				result.append([r,c])
				
		right = False
	else:
		for i in range(1,dis+1):
			c = c-1
			if(r>=R or c >= C or c<0 or r<0):
				pass
			else:
				visited[r][c] = True
				result.append([r,c])
				
		for i in range(1,dis+1):
			r = r-1
			if(r>=R or c >= C or c<0 or r<0):
				pass
			else:
				visited[r][c] = True
				result.append([r,c])
				
		right = True
	dis += 1
print(result)