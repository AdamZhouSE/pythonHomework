strs=eval(input())
res=[]
res.append([strs[0]])
leng=len(strs)
flag=False
fflag=True
for i in range(1,leng):
    fflag=True
    s=strs[i]
    for j in range(len(res)):
        for k in range(len(res[j])):
            tmp=[]
            stmp=[]
            flag=False
            for l in range(len(s)):
                if(s[l]!=res[j][k][l]):
                    stmp.append(s[l])
                    tmp.append(res[j][k][l])
            stmp.sort()
            tmp.sort()
            if(len(stmp)==2  or len(stmp)==0) and stmp==tmp:
                flag=True
                break
        if(flag):
            res[j].append(s)
            fflag=False
            break
    if(fflag):
        res.append([s])
print(len(res))

