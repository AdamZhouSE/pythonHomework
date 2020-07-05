from itertools import combinations
source_1=list(input())
source_2=list(input())
target_1=[]
for i in range(len(source_1)):
    target_1.append(i)
target_1_1=[]
for i in range(1,len(source_1)+1):
    a=list(combinations(target_1,i))
    for j in a:
        target_1_1.append(list(j))
target_2=[]
for i in range(len(source_2)):
    target_2.append(i)
target_2_2=[]
for i in range(1,len(source_2)+1):
    a=list(combinations(target_2,i))
    for j in a:
        target_2_2.append(list(j))
targets_1=[]
for i in target_1_1:
    a=[]
    for j in i:
        a.append(source_1[j])
    if(not a in targets_1):
        targets_1.append(a)
targets_2=[]
for i in target_2_2:
    a=[]
    for j in i:
        a.append(source_2[j])
    if(not a in targets_2):
        targets_2.append(a)
res=[]
for i in targets_1:
    for j in targets_2:
        if(len(i)==len(j)):
            counts=0
            for x in range(len(i)):
                if(i[x]!=j[x]):
                    counts=counts+1
            if(counts!=1):
                res.append([i,j])
for i in res:
    i.sort()
ans=[]
for i in res:
    if(not i in ans):
        ans.append(i)
print(len(ans))
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    