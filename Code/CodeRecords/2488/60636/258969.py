sources=eval(input())
res=[]
print(sources)
res.append(sources[0])
sources.pop(0)
for i in range(1,len(sources)):
    print(res)
    print(sources)
    if(i%2==1):
        for j in range(len(sources)):
            if(sources[j]>res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
        else:
            continue
    else:
        for j in range(len(sources)):
            print(sources[j])
            if(sources[j]<res[-1]):
                res.append(sources[j])
                sources.pop(j)
                break
        else:
            continue
print(res)
























