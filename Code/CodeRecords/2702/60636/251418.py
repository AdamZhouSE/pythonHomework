def find(sources):
    for i in range(len(sources)):
        for j in range(len(sources[i])):
            if(sources[i][j]=="1"):
                return [i,j]
    else:
        return -1
def flood(sources,location):
    target=[]
    target.append(location)
    while(len(target)!=0):
        print(target)
        targets=target.copy()
        for i in range(len(target)):
            if(sources[target[i][0]][target[i][1]+1]=="1"):
                sources[target[i][0]][target[i][1]+1]=="0"
                targets.append([target[i][0],target[i][1]+1])
            if(sources[target[i][0]][target[i][1]-1]=="1"):
                sources[target[i][0]][target[i][1]-1]=="0"
                targets.append([target[i][0],target[i][1]-1])
            if(sources[target[i][0]+1][target[i][1]]=="1"):
                sources[target[i][0]+1][target[i][1]]=="0"
                targets.append([target[i][0]+1,target[i][1]])
            if(sources[target[i][0]-1][target[i][1]]=="1"):
                sources[target[i][0]-1][target[i][1]]=="0"
                targets.append([target[i][0]-1,target[i][1]])
            targets.pop(0)
        target=targets
sources=[]
try:
    while(True):
        x=list(input())
        sources.append(x)
except(EOFError):
    pass
count=0
while(find(sources)!=-1):
    print(sources)
    count=count+1
    flood(sources,find(sources))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    