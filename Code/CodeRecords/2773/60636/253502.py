source=[]
while(True):
    x=input()[:-1]
    if(x=="]"):
        break
    elif(x!="["):
        x=eval(x)
        source.append(x)
alls=[]
res=[]
print(source)
for i in source:
    ress=[]
    for j in i:
        print(j)
        ress.append(0)
        if(not j in alls):
            alls.append(j)
    res.append(ress)
alls.sort()
for i in alls:
    for a in range(len(source)):
        for b in range(len(source[a])):
            if(source[a][b]==i):
                if(i==alls[0]):
                    res[a][b]=1
                else:
                    ans=[]
                    ans.append(1)
                    if a==0 and b==0:
                        if(source[a][b+1]<source[a][b]):
                            ans.append(res[a][b+1]+1)
                        if(source[a+1][b]<source[a][b]):
                            ans.append(res[a+1][b]+1)
                    elif a==0 and b==len(source[a])-1:
                        if source[a+1][b]<source[a][b]:
                            ans.append(res[a+1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                    elif a==len(source)-1 and b==0:
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a][b+1]<source[a][b]:
                            ans.append(res[a][b+1]+1)
                    elif a==len(source)-1 and b==len(source[a])-1:
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                    elif a==0:
                        if source[a+1][b]<source[a][b]:
                            ans.append(res[a+1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                        if source[a][b+1]<source[a][b]:
                            ans.append(res[a][b+1]+1)
                    elif a==len(source):
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                        if source[a][b+1]<source[a][b]:
                            ans.append(res[a][b+1]+1)
                    elif b==0:
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a+1][b]<source[a][b]:
                            ans.append(res[a+1][b]+1)
                        if source[a][b+1]<source[a][b]:
                            ans.append(res[a][b+1]+1)
                    elif b==len(source[a])-1:
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a+1][b]<source[a][b]:
                            ans.append(res[a+1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                    else:
                        if source[a-1][b]<source[a][b]:
                            ans.append(res[a-1][b]+1)
                        if source[a+1][b]<source[a][b]:
                            ans.append(res[a+1][b]+1)
                        if source[a][b-1]<source[a][b]:
                            ans.append(res[a][b-1]+1)
                        if source[a][b+1]<source[a][b]:
                            ans.append(res[a][b+1]+1)
                    res[a][b]=max(ans)
maxs=1
for i in res:
    for j in i:
        if j>maxs:
            maxs=j
print(maxs)