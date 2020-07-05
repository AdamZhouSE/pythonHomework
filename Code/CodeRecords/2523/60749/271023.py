mat=input()
def diagonalSort(mat):
    m=len(mat)
    n=len(mat[0])
    for i in range(m):
        for j in range(n):
            if i>0 and j>0:
                continue
            temp=[]
            a=i
            b=j
            while a<m and b<n:
                temp.append(mat[a][b])
                a+=1
                b+=1
            temp=sorted(temp)
            a=i
            b=j
            index=0
            while a<m and b<n:
                mat[a][b]=temp[index]
                index+=1
                a+=1
                b+=1
    return mat
print(diagonalSort(mat))