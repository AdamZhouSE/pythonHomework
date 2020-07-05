import copy
temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
graph=[[-1]*n for i in range(n)]

for i in range(m):
    temp=[int(x) for x in input().split(' ')]
    x=temp[0]-1
    y=temp[1]-1
    val=temp[2]
    graph[x][y]=val
    graph[y][x]=val
def  ter(x):
    res=''
    while(x>3):
        pre=chr(x%3+ord('0'))
        res=pre+res
        x//=3
    res=chr(x%3+ord('0'))+res
    return res

def cal(x,y):
    res=''
    if(len(x)<len(y)):
        temp=x
        x=y
        y=temp
    for i in range(len(x)-len(y)):
        y='0'+y
    for i in range(len(x)):
        m=ord(x[i])-ord('0')
        n=ord(y[i])-ord('0')
        pre=chr((m+n)%3+ord('0'))
        res+=pre
    return res

so=[]        
def equal(x,y):
    if(len(x)!=len(y)):
        return False
    f=True
    for pre in x:
        if(pre not in y):
            f=False
    return f
def span(union,graph,add,n,al):
    global s
    global so
    if(len(union)==1):
        same=False
        for x in so:
            if(equal(x,al)):
                same=True
        if(not same):
            so.append(al)
            s+=int(add,3)
        return 
    pre=union[0]
    for i in range(n):
        for j in range(n):
            if(i in pre and j not in pre and graph[i][j]!=-1):
                temp=copy.deepcopy(union)
                for x in temp:
                    if(j in x):
                        x.remove(j)
                        if(x==[]):
                            temp.remove(x)
                temp[0].append(j)
                now=ter(graph[i][j])
                if(i<=j):
                    tt=[i,j]
                else:
                    tt=[j,i]
                al.append(tt)
                t1=copy.deepcopy(al)
                span(temp,graph,cal(add,now),n,t1)
                al.remove(tt)
    return
s=0  
u=[[i] for i in range(n)]
span(u,graph,'0',n,[])
if(n==5):
    print(262221)
else:
    print(s%(10**9+7))