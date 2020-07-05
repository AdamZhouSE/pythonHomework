strs=eval(input())
ans=True
tmp=0
res={}
for i in range(len(strs)):
    a=strs[i][0]
    b=strs[i][3]
    sign=strs[i][1]
    if(sign=='='):
        if(a not in res.keys()):
            res[a]=tmp
            tmp+=1
        if(b not in res.keys()):
            res[b]=res[a]
        else:
            if(res[b]!=res[a]):
                ans=False
                break
    elif(sign=='!'):
        if (a not in res.keys()):
            res[a] = tmp
            tmp += 1
        if (b not in res.keys()):
            res[b] = tmp
            tmp+=1
        else:
            if (res[b] == res[a]):
                ans = False
                break
if(ans):
    print("true")
else:
    print("false")