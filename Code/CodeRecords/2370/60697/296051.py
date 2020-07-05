K=int(input())
res=[]
while K!=0:
    mo=K%(-2)
    pro=K//(-2)
    if(mo==-1):
        mo=1
        pro=pro+1
    res.insert(0,str(mo))
    K=pro
print("".join(res))
