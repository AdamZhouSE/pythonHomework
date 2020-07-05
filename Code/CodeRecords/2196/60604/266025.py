x=input().split()
hang=int(x[0])
lie=int(x[1])
mat=[]
for i in range(hang):
    x=list(input())
    mat.append(x)
#print(mat)
tmp1=[]
res=[]
for i in range(1,hang):
    for j in range(1,lie):
        tmp1=[]
        for k in range(hang-i):
            for l in range(lie-j):
                tmp=mat[k][l:l+j]
                tmp1.append(tmp)
                
        if not tmp1 in res:
            res.append(tmp1)
print(res)
print(len(res))