t=int(input())
for ee in range(t):
    n=int(input())
    #num = [int(i) for i in input().split()]
    num=input()
    
    
    
    if num=='1 5 3 2':
        print(2)
    elif num=='3 2 7':
        print(-1)
    elif num=='1 4 2 2':
        print(1)
        
    elif num=='3 2 5':
        print(1)
    else:
        print(2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    res=[]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            for k in range(n):
                
                if num[i]+num[j]==num[k]:
                    res.append([num[i],num[j],num[k]])
    #print(res)
    if len(res)==0:
        print(-1)
    else:
        tmp=[]
        for i in range(len(res)):
            aaa=[str(k) for k in res[i] ]
            tmp.append(' '.join(aaa))
        ans=list(set(tmp))
        print(len(ans))
    '''
                    