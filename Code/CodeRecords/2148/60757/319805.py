import math
class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
def calb(s):
    n=len(s)
    if n==1:
        li=[]
        if s=='+':
            li.append('0')
            return li
        elif s=='-':
            li.append('1')
            return li
        else:
            li.append('0')
            li.append('1')
            return li
    else:
        a=s[0]
        li=calb(s[1:])
        t=len(li)
        if a=='+':
            for i in range(t):
                li[i]='0'+li[i]
            return li
        elif a=='-':
            for i in range(t):
                li[i]='1'+li[i]
            return li
        else:
            for i in range(t):
                li.append(li[i])
            for i in range(t):
                li[i]='0'+li[i]
            for i in range(t,2*t):
                li[i]='1'+li[i]
            return li
def calf(li,s):
    n=len(s)
    for i in range(n):
        if s[i]=='+':
            for j in range(len(li)):
                li[j]=li[j][0:i]+'0'+li[j][i+1:]
        if s[i]=='-':
            for j in range(len(li)):
                li[j]=li[j][0:i]+'1'+li[j][i+1:]
    return li

def trans(s):
    re=0
    for i in range(len(s)):
        re=re*2
        if s[i]=='1':
            re+=1
    return re            
            
        
def dij(graph,a):
    n=len(graph.matrix)
    re=[]
    for i in range(n):
        re.append(-1)
    sure=[]
    for i in range(n):
        sure.append(0)
    re[a-1]=0
    sure[a-1]=1
    tmp=a
    k=0
    while(k!=n-1):
        for i in range(n):
            if graph.matrix[tmp-1][i]>0:
                if re[i]==-1 or re[tmp-1]+graph.matrix[tmp-1][i]<re[i]:
                    re[i]=re[tmp-1]+graph.matrix[tmp-1][i]
        minind=-1
        minl=-1
        for i in range(n):
            if sure[i]==0:
                if re[i]>0:
                    if minl==-1 or re[i]<minl:
                        minl=re[i]
                        minind=i
        if minind==-1:
            break
        sure[minind]=1
        tmp=minind+1
        k+=1
    return re           
    
li=input().split()
n=int(li[0])
m=int(li[1])
t1=[]
g=[]
al=int(math.pow(2,n))
for i in range(al):
    t1.append(-1)
for i in range(al):
    t=t1[:]
    g.append(t)
for i in range(m):
    li=input().split()
    time=int(li[0])
    s1=calb(li[1])
    new1=[]
    for j in range(len(s1)):
        tmp=trans(s1[j])
        new1.append(tmp)
    ll=s1[:]
    s2=calf(ll,li[2])
    new2=[]
    for j in range(len(s2)):
        tmp=trans(s2[j])
        new2.append(tmp)
    for j in range(len(s1)):
        g[new1[j]][new2[j]]=time
for i in range(al):
    g[i][i]=0
graph=Graph(g)
tmp=dij(graph,1)
if tmp[al-1]==-1:
    print('0')
else:
    print(tmp[al-1])
    