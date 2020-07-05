sources=eval(input())
res=[]
n=len(sources)
res.append(min(sources))
sources.pop(sources.index(min(sources)))
for i in range(1,n):
    if(i%2==1):
        for j in range(len(sources)):
            if(sources[j]>res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
    else:
        for j in range(len(sources)):
            if(sources[j]<res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
print(res)
























