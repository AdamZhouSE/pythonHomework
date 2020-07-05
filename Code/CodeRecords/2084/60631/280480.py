a=input().split(' ')
n=int(a[0])
m=int(a[1])
s=int(a[2])
t=int(a[3])
G={}
for mi in range(m):
    l=input().split(' ')
    mid={}
    mid[int(l[1])]=int(l[2])
    G[int(l[0])]=mid
print(G)
inf=99999
length=[]
length.append(inf)
length.append(0)
for i in range(m):
    length.append(inf)
Q=[]



def branch(G,v0):
    Q.append(v0)
    dict = G[1]
    while len(Q)!=0:
        head=Q[0]
    for key in dict:
        if length[head]+G[head][key] <= length[key]:
            length[key]=length[head]+G[head][key]
            Q.append(key)
    del Q[0]
    if len(Q)!=0:
        dict=G[Q[0]]

branch(G,s)
print(length[t-1])
    
    
    
    

















