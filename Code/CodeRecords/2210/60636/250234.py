t=int(input())
for a in range(t):
    sources=list(input())
    targets=list(input())
    lists=[]
    for i in targets:
        source=[]
        for j in range(len(sources)):
            if(i==sources[j]):
                source.append(j)
        lists.append(source)
    starts=[]
    for i in lists:
        starts.append(min(i))
    ends=[]
    for i in lists:
        ends.append(max(i))
    start=min(starts)
    end=max(ends)
    new_source=sources[start:end+1]
    print(new_source)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    