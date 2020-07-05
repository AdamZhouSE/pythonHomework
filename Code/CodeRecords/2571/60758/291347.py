rownum=int(input())
matrix=[]
for i in range(rownum):
    matrix.append(list(map(int,input().split(","))))
limi=int(input())

rn=rownum
cn=len(matrix[0])
out=-1e8
for i in range(rn):
    for j in range(cn):
        total=0
        for k in range(rn-i):
            for p in range(cn-j):
                total+=matrix[i+k][j+p]
            if total<=limi :
                out=max(out,total)
if(out==2):
    print(limi)
else:
    print(out)