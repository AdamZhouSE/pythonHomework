line=int(input())
matrix=[]
for x in range(0,line):
    y=list(map(int,input().split(",")))
    for i in y:
        matrix.append(i)
matrix.sort()
k=int(input())
print(matrix[k-1])