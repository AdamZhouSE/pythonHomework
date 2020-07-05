n_m_q=list(input())
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
    b=int(y[0])
    available.append([a,b])
    dcc[a-1].append(b)
    dcc[b-1].append(a)
for i in range(q):
    x=input().split(" ")
    l=int(x[0])
    r=int(x[1])
    s=int(x[2])
    t=int(x[3])
    
        