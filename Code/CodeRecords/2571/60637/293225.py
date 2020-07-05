n=(int)(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split(','))))
k=(int)(input())
m=len(matrix[0])
def rectangule(i,u,j,v):
    global matrix
    sum=0
    for x in range(i,u):
        for y in range(j,v):
            sum+=matrix[x][y]
    return sum
record=-float('Inf')
for i in range(n):
    for j in range(m):
        for u in range(i+1,n+1):
            for v in range(j+1,m+1):
                temp=rectangule(i,u,j,v)
                if(temp>record and temp<=k):
                    record=temp
print(record)
