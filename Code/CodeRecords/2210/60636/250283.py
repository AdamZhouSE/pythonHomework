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
    length=len(new_source)+1
    while(length!=len(new_source)):
        length=len(new_source)
        for i in targets:
            sum=0
            location=[]
            for a in range(len(new_source)):
                if(new_source[a]==i):
                    location.append(a)
                    sum=sum+1
            print(location)
            delete=True
            if(sum>1):
                for y in targets:
                    if(y!=i):
                        if(not y in new_source[location[1]:]):
                            delete=False
                if(delete):
                    new_source=new_source[location[1]:]
        for i in targets:
            sum=0
            location=[]
            for a in range(len(new_source)-1,0,-1):
                if(new_source[a]==i):
                    location.append(a)
                    sum=sum+1
            delete=True
            if(sum>1):
                for y in targets:
                    if(y!=i):
                        if(not y in new_source[:location[1]+1]):
                            delete=False
                if(delete):
                    new_source=new_source[:location[1]+1]
    res=""
    for i in new_source:
        res=res+i
    print(res)
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    