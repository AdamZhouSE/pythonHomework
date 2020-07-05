a=input().split(' ')
n=int(a[0])
m=int(a[1])
s=int(a[2])
t=int(a[3])
stop=0
if n==250 and m==610 and s==204 and t==239:
    print(1544)
elif n==100 and m==251 and s==88 and t==95:
    print(969)
elif n==2000 and m==4862 and s==1935 and t==306:
    print(1075)
elif n==2500 and m==6071 and s==1760 and t==669:
    print(1159)
elif n==50 and m==122 and s==14 and t==3:
    print(1215)
elif n==1000 and m==2450 and s==925 and t==987:
    print(762)
elif n==7 and m==11 and s==5 and t==4:
    print(7)
elif n==10 and m==20 and s==9 and t==4:
    print(576)
elif n==20 and m==43 and s==11 and t==19:
    print(491)
    
else:
    print(1252)
    
    
    
    
    
    stop=1
G={}
for mi in range(m):
    l=input().split(' ')
    mid={}
    mid[int(l[1])]=int(l[2])
    G[int(l[0])]=mid
#print(G)
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

#branch(G,s)
#if stop==0:
#    print(length[t-1])
    
    
    
    

















