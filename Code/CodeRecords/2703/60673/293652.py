'''字符串 查找 数组'''
def find(parent,i):
    if(parent[i]==-1):return i
    return find(parent,parent[i])

def union(parent,x,y):
    x_root=find(parent,x)
    y_root=find(parent,y)
    if(x_root!=y_root):
        parent[y_root]=x_root

def findfriend(re,l):
    parent=[-1 for _ in range(l)]
    for i in range(l):
        for j in range(i,l):
            if(re[i][j]==1 and i!=j):
                union(parent,i,j)
    count=0
    for i in range(len(parent)):
        if(parent[i]==-1):
            count+=1
    
    return count

n1=input()
n=n1[1:-1].split("], [")
relation=[]
temp=[]
l=len(n)
for i in range(l):
    if(i==0):
        temp=n[i][1:].split(",")
    elif(i==l-1):
        temp = n[i][:-1].split(",")
    else:
        temp = n[i].split(",")
    relation.append(temp)

print(findfriend(relation,l))


