sources=list(input())
res=[]
res.append(sources[0])
sources.pop(0)
while(len(sources)!=0):
    a=len(res)
    n=len(sources)
    for i in range(n):
        if sources[i]!=res[-1]:
            res.append(sources[i])
            sources.pop(i)
            break
    if(len(res)==a):
        break
if(len(sources)!=0):
    print("")
else:
    ans=""
    for i in res:
        ans=ans+i
    print(ans)