matrix=eval(input())
n=len(matrix[0])
m=len(matrix)
for i in range(n):
    start=matrix[0][i]
    sortset=[]
    sortset.append(start)
    index1=1
    index2=i+1
    while(index1<=m-1 and index2<=n-1):
        sortset.append(matrix[index1][index2])
        index1+=1
        index2+=1
    sortset.sort()
    for j in range(len(sortset)):
        matrix[j][i+j]=sortset[j]
for i in range(1,m):
    start=matrix[i][0]
    sortset = []
    sortset.append(start)
    index1 =i+1
    index2 =1
    while (index1 <= m- 1 and index2 <= n - 1):
        sortset.append(matrix[index1][index2])
        index1 += 1
        index2 += 1
    sortset.sort()
    for j in range(len(sortset)):
        matrix[i+j][j]=sortset[j]
print(matrix)