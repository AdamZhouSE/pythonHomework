def delete(matrix,aim,dim,root):
    answer=0
    if matrix.__len__()==aim:
        for i in matrix:
            answer+=i[2]
        print(answer)
        return
    else:
        nodes=[[0,-1] for i in range(dim)]
        nodes[root][0]+=1
        canDel=[]
        for i in matrix:
            nodes[i[0]-1][0]+=1
            nodes[i[0] - 1][1]=matrix.index(i)
            nodes[i[1]-1][0]+=1
            nodes[i[1] - 1][1]=matrix.index(i)
        for i in range(dim):
            if nodes[i][0]==1:
                canDel.append(nodes[i][1])
        min=canDel[0]
        for i in canDel:
            if matrix[i][2]<matrix[min][2]:
                min=i
        matrix.pop(min)
        delete(matrix,aim,dim,root)
line=input().split()
n=int(line[0])
k=int(line[1])
matrix=[]
root=0
for i in range(n-1):
    line2=input().split()
    line2=[int(x) for x in line2]
    if i==0:
        root=line2[0]-1
    matrix.append(line2)
delete(matrix,k,n,root)