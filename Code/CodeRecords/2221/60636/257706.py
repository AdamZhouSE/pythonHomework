n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
sources=[]
for i in range(m):
    x=input().split(" ")
    sources.append(x)
res=[]
for i in range(1,n+1):
    ans=[]

    ans.append(str(i))
    result=[]
    while(len(ans)>0):
        a=[]
        for y in ans:
            if not y in result:
                result.append(y)
                for x in sources:
                    if(x[0]==y):
                        if not x[1] in result and not x[1] in ans:
                            a.append(x[1])
        ans=a
    res.append(result)
counts=[]
for i in range(n):
    counts.append(0)
for i in res:
    for j in i[1:]:
        counts[int(j)-1]+=1
count=0
for i in counts:
    if(i==n-1):
        count+=1
print(count)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
