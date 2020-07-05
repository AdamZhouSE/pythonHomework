# 求最大流 Ford-Fulkerson算法 和离散数学学的标号算法应该是一个
class edge:
    def __init__(self,to,value,rev_edge):
        self.to=to
        self.value=value
        self.rev_edge=rev_edge

def insert(a,b):# 即使插入多次a,b也没关系
    global v
    v[a].append(edge(b,1,len(v[b])))# len(v[b])就可以算出接下来要插入的反向边在v[b]中的序号
    v[b].append(edge(a,0,len(v[a])-1))
    return

def search(now,target,flow):
    global v,visited
    if now==target:
        return flow
    visited[now]=True
    for i in range(0,len(v[now])):
        tmp=v[now][i] #这里是引用吗？
        if (not visited[tmp.to]) and tmp.value>0:
            t=search(tmp.to,target,min(flow,tmp.value))
            if t>0:
                tmp.value-=t
                v[tmp.to][tmp.rev_edge].value+=t
                return t
    return 0

n,m=map(int,input().split())
v=[[]for i in range(0,n+2)]# 0是源点，n+1是汇点
while True:
    try:
        a,b=map(int,input().split())
        insert(a,b)
    except:
        break
for i in range(1,m+1):
    insert(0,i)
for i in range(m+1,n+1):
    insert(i,n+1)
total=0
t=999999999
while t!=0:
    visited=[False for i in range(0,n+2)]
    t=search(0,n+1,999999999)
    total+=t
print(total)