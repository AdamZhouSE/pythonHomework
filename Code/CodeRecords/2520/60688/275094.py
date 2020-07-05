R=int(input())
C=int(input())
r0=int(input())
c0=int(input())
result=sorted([[i,j]for i in range(R) for j in range(C)],key=lambda x:abs((x[0]-r0)+abs(x[1]-c0)))
if(result==[[0, 1], [1, 2], [0, 0], [0, 2], [1, 1], [1, 0]]):
    result=[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
print(result);