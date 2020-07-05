from itertools import combinations
t=int(input())
for j in range(t):
    number=int(input())
    source=input().split(" ")
    sources=[]
    for i in source:
        sources.append(int(i))
    lists=[]
    for i in range(number):
        lists.append(i)
    targets=[]
    for i in range(int(number/2),number):
        target=list(combiniations(lists,i))
        for h in target:
            if((h[-1]==number-1)|(h[-1]==number-2)):
                may=True
                for k in range(len(h)-1):
                    if(h[k+1]-h[k]>=3):
                        may=False
                if(may):
                    z=[]
                    for a in h:
                        z.append(sources[a])
                    targets.append(z)
    sums=[]
    for i in targets:
        sum=0
        for a in i:
            sum=sum+a
        sums.append(sum)
    print(min(sums))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        