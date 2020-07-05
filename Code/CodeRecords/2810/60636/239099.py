number=input()
sources=[]
numbers=list(number)
for i in range(len(numbers)):
    source=[]
    for a in range(int(numbers[i])):
        source.append(int("1"+"0"*(len(numbers)-i-1)))
    sources.append(source)
res=[]
while(len(sources)!=0):
    for i in range(len(sources)-1,0,-1):
        if(len(sources[i])>len(sources[0])):
            for a in range(len(sources[0])):
                sources[0][a]=sources[0][a]+sources[i][0]
            for x in range(len(sources[0])):
                sources[i].pop(0)
        elif(len(sources[i])<=len(sources[0])):
            for a in range(len(sources[i])):
                sources[0][a]=sources[0][a]+sources[i][0]
            sources.pop(i)
    res.append(sources[0])
    sources.pop(0)
result=[]
for i in range(len(res)):
    for a in range(len(res[i])):
        result.append(res[i][a])
print(len(result))
print(*result)
    
    
    
    
    
    
    
    
    
    
    
    