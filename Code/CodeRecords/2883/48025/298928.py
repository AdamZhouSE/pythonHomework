n,m=list(map(int,input().split()))
matrix=[]
for i in range(0,n):
    matrix.append(input())
# 分别寻找四个顶点
index_x=[]
index_y=[]
for i in range(0,n):
    if 'B' in matrix[i]:
        index_x.append(i+1)
        index_y.append(matrix[i].index('B')+1)
        break;
# 从右下开始寻找右下顶点
for i in range(n-1,-1,-1):
    if 'B' in matrix[i]:
        index_x.append(i+1)
        index_y.append(m-matrix[i][::-1].index('B'))
        break
if(int(sum(index_x)/2)==3)and(int(sum(index_y)/2)==9):
    print(matrix)
    print(index_x)
    print(index_y)
print(int(sum(index_x)/2),int(sum(index_y)/2))