"""并查集"""
def findfriend(re,l):
    parent=[-1 for _ in range(l)]

    def find(parent, i):
        if (parent[i] == -1): return i
        return find(parent, parent[i])

    def union(parent, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if (x_root != y_root):
            parent[y_root] = x_root
    
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
re=[]
temp=[]
l=len(n)
for i in range(l):
    if(i==0):
        temp=n[i][1:].split(",")
    elif(i==l-1):
        temp = n[i][:-1].split(",")
    else:
        temp = n[i].split(",")
    for i in range(l):
        temp[i]=int(temp[i])
    re.append(temp)

print(findfriend(re,l))


