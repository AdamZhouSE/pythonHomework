x=input().split()
hang=int(x[0])
lie=int(x[1])
mat=[]
for i in range(hang):
    x=list(input())
    mat.append(x)
#print(mat)
mat=[['A','B','A'],['B','A','A'],['A','A','A']]
hang=3
lie=3

tmp1=[]
res=[]
for i in range(1,hang):
    for j in range(1,lie):
        tmp1=[]
        tmp2=[]
        for k in range(hang-i+1):
            tmp=mat[k:k+i]
        for l in range(lie-j+1):
            for m in tmp:
                tmp1.append(m[l:l+j])
        print(tmp1)        
        if not tmp1 in res:
            res.append(tmp1)
print(res)
print(len(res))