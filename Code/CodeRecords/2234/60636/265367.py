n=int(input())
p=int(input())
jiandie=[]
starts=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    starts.append(int(x[0])-1)
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
res=[]
for i in range(len(starts)):
    first=starts[i]
    may=starts.copy()
    may.pop(may.index(first))
    alls=[]
    ress=[]
    target=[]
    target.append(first)
    while(len(may)):
        if(len(target)==0):
            target.append(may[0])
            may.pop(0)
        ans=[]
        while(len(target)):
            x=target.copy()
            print("target")
            
            print(target)
            print("ans")
            print(ans)
            print("alls")
            print(alls)
            for a in target:
                if not a in alls:
                    ans.append(a)
                    alls.append(a)
                    x.pop(x.index(a))
                    for i in range(len(sources[a])):
                        if sources[a][i]=="1":
                            if not i in ans or not i in target or not i in alls:
                                x.append(i)
                                if(i in may):
                                    may.pop(may.index(i))
            target=x
        ress.append(ans)
    print(ress)
    print(alls)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    