def findKmin(Matrix, k):
    contrast = []
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            contrast.append(Matrix[i][j])
    for i in range(k-1):
        Min=min(contrast)
        for j in range(len(contrast)):
            if contrast[j]==Min:
                del(contrast[j])
                break
    return min(contrast)

size=int(input())
Matrix=[]
for i in range(size):
    List=list(map(int,input().split(',')))
    Matrix.append(List)
k=int(input())
print(findKmin(Matrix,k))
