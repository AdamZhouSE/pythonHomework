source_1=list(input())
source_2=list(input())
targets_1=[]
for i in range(1,len(source_1)+1):
    for j in range(len(source_1)-i+1):
        targets_1.append([j:j+i])
targets_2=[]
for i in range(1,len(source_2)+1):
    for j in range(len(source_2)-i+1):
        targets_2.append([j:j+i])
res=[]
for i in targets_1:
    for j in targets_2:
        if(i==j):
            res.append(i)
print(len(res))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    