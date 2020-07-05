import collections
t=list(map(int,input().split(' ')))
size=t[0]
instrsize=t[1]
res=list(map(int,input().split(' ')))
res.insert(0,0)
parent=[i for i in range(size+1)]
child=[i for i in range(size+1)]
childs=collections.defaultdict(set)

def parentsum(x):
    sum = 0
    sum+=res[x]
    while parent[x]!=x:
        sum+=res[parent[x]]
        x=parent[x]
    return sum

def addchild(x,addnum):
    res[x]+=addnum
    if(x in childs.keys()):
        for i in childs[x]:
            addchild(i,addnum)
def union(x,y):
    parent[y]=x
for i in range(size-1):
    a=list(map(int,input().split(' ')))
    childs[a[0]].add(a[1])
    union(a[0],a[1])
instrs=[]
for i in range(instrsize):
    instrss=input().split(' ')
    a=[]
    for j in instrss:
        if(j!=''):
            a.append(int(j))
    instrs.append(a)
for i in range(instrsize):
    instr=instrs[i][0]
    if(instr==1):
        index=instrs[i][1]
        addnum=instrs[i][2]
        res[index]+=addnum
    elif(instr==2):
        index = instrs[i][1]
        addnum = instrs[i][2]
        addchild(index,addnum)
    elif(instr==3):
        index = instrs[i][1]
        sum=parentsum(index)
        print(sum)



