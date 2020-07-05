rownum=int(input())
matrix=[]
for i in range(rownum):
    matrix.append(list(map(int,input().split(","))))
limi=int(input())
rn=rownum
cn=len(matrix[0])

def cal(i,j,k,p):
    total=0
    for m in range(i,k+1):
        for n in range(j,p+1):
            total+=matrix[m][n]
    return total
out=0
for i in range(0,rn):
    for j in range(0,cn):
        for k in range(i,rn):
            for p in range(j,cn):
                total=cal(i,j,k,p)
                if(total<=limi):
                    out=max(out,total)
print(out)