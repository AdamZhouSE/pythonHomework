n_m_q=input().split(" ")
n=int(n_m_q[0])
m=int(n_m_q[1])
q=int(n_m_q[2])
dcc=[]
for i in range(n):
    a=[]
    dcc.append(a)
available=[]
for i in range(m):
    x=input().split(" ")
    a=int(x[0])
    b=int(x[0])
    available.append([a,b])
    dcc[a-1].append(b)
    dcc[b-1].append(a)
print(dcc)
for i in range(q):
    x=input().split(" ")
    l=int(x[0])
    r=int(x[1])
    s=int(x[2])
    t=int(x[3])
    target=[]
    target.append(s)
    for j in range(l-1,r):
        x=[]
        for a in target:
            x.append(a)
            for y in dcc[a-1]:
                if [a,y] in available:
                    if available.index([a,y])==j:
                        x.append(y)
                if [y,a] in available:
                    if available.index([y,a])==j:
                        x.append(y)
        target=x
    print(target)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        