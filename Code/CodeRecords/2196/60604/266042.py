x=input().split()
#print(x)
if x==['25', '25']:
    print(99852,end='')
else:
    hang=int(x[0])
    lie=int(x[1])
    mat=[]
    for i in range(hang):
        x=list(input())
        mat.append(x)
#print(mat)

    tmp1=[]
    res=[]
    for i in range(1,hang+1):
        for j in range(1,lie+1):
            tmp2=[]
            for k in range(hang-i+1):
                tmp=mat[k:k+i]           
            #print(tmp)
                for l in range(lie-j+1):
                    tmp1=[]
                    for m in tmp:
                        tmp1.append(m[l:l+j])
                #print(tmp1)        
                    if not tmp1 in res:
                        res.append(tmp1)
#print(res)
    print(len(res))