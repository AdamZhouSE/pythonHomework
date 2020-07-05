t=list(map(int,input().split(' ')))
instrnum=t[0]
init=t[1]
res=[]
for i in range(instrnum):
    res.append(list(map(int,input().split(' '))))
res.sort(key=lambda x:x[0])
tmp={}
maxsize=0
ans=0
a=[]
ttmp={}

for i in range(instrnum):
    b = []
    coat=res[i][1]
    if coat not in tmp:
        pro=res[i][2]+init
        tmp[coat]=pro
    else:
        tmp[coat]=tmp[coat]+res[i][2]
    ttmp=sorted(tmp.items(),key=lambda x:x[1],reverse=True)
    maxsize=ttmp[0][1]
    for i in range(len(ttmp)):
        if(ttmp[i][1]!=maxsize):
            break
        else:
            b.append(ttmp[i][0])
    if(a!=b):
        ans+=1
    a=b
print(ans,end="")




