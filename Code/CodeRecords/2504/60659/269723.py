import re
list1 = input()
pattern = re.compile('\-\d+|\d+')
A = pattern.findall(list1)
k=int(input())
points=[]
counter=0
distence=[]
result=[]
while counter<len(A):
	points.append([int(A[counter]),int(A[counter+1])])
	distence.append(int(A[counter])*int(A[counter])+int(A[counter+1])*int(A[counter+1]))
	counter+=2
num=sorted(distence)
for i in range(k):
	result.append(points[distence.index(num[i])])
print(result)