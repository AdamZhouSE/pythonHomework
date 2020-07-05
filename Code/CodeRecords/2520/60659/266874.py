r=int(input())
c=int(input())
r0=int(input())
c0=int(input())
matrix=[]
result=[[r0,c0]]
for i in range(r):
	for j in range(c):
		matrix.append([i,j])
counter=1
while len(result)<r*c:
	for i in range(len(matrix)):
		if abs(matrix[i][0]-r0)+abs(matrix[i][1]-c0)==counter:
			result.append(matrix[i])
	counter+=1
print(result)