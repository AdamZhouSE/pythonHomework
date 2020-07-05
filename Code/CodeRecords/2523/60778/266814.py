mat=eval(input())
m=len(mat)
n=len(mat[1])
size=min(m,n)
for ptr in range(0,m):
    tmp=[mat[ptr,0]]
    for i in range(1,size-ptr):
        tmp.append(mat[ptr+i][i])
    tmp.sort()
    for i in range(0,size-ptr):
        mat[ptr+i][i]=tmp[i]
for ptr in range(0,n):
    tmp=[mat[ptr,0]]
    for i in range(1,size-ptr):
        tmp.append(mat[i][ptr+i])
    tmp.sort()
    for i in range(0,size-ptr):
        mat[i][ptr+i]=tmp[i]
print(mat)