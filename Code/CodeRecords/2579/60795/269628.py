m=int(input())
mat=[]
for i in range(0,m):
    arr=[int(n) for n in input().split(',')]
    mat.append(arr)
n=len(mat[0])
threshold=int(input())
side,maxside=1,0
while side<=m and side<=n:
    for i in range(0,n):
        sum=0
        if i+side-1<m and i+side-1<n:
            for j in range(i,i+side):
                for k in range(i,i+side):
                    sum=sum+mat[j][k]
            if sum<=threshold:
                if side>maxside:
                    maxside=side
    side=side+1
print(maxside)