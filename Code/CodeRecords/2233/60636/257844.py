n=int(input())
sources=[]
for i in range(n):
    x=input().split(" ")
    sources.append(x)
res=[]
alls=[]
for i in range(n):
    if not i in alls:
        ans=[]
        target=[]
        target.append(i)
        while(len(target)>0):
            a=[]
            for j in target:
                if not sources[j] in ans:
                    ans.append(j)
                    for x in range(len(sources[j])):
                        if sources[j][x]=="1":
                            if not x in a and not x in ans:
                                a.append(x)
            target=a
        res.append(res)
        for i in res:
            if not i in alls:
                alls.append(i)
print(len(res))
                
        