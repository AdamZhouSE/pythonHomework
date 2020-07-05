t=int(input())
for i in range(t):
    string_1=list(input())
    string_2=list(input())
    all_1=[]
    all_2=[]
    alls=[]
    for j in string_1:
        if(not j in all_1):
            all_1.append(j)
        if(not j in alls):
            alls.append(j)
    for j in string_2:
        if(not j in all_2):
            all_2.append(j)
        if(not j in alls):
            alls.append(j)
    res=[]
    for j in alls:
        if((not j in all_1)|(not j in all_2)):
            res.append(j)
    res.sort()
    ans=""
    for j in res:
        ans=ans+j
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    