mat=[]
for i in range(0,4):
    mat.append(list(map(int,input().split(","))))
sum=0
length=len(mat[0])
for i in range(0,length):
    for j in range(0,length):
        for k in range(0,length):
            for t in range(0,length):
                if mat[0][i]+mat[1][j]+mat[2][k]+mat[3][t]==0:
                    sum+=1
print(sum)