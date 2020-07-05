def findMax(tree):
    res=[1]
    while len(tree)!=0:
        group=[]
        group.append(tree.pop(0))
        i=0
        while i<len(group):
            j=0
            while j<len(tree):
                if tree[j][0] in group[i] or tree[j][1] in group[i]:
                    group.append(tree.pop(j))
                else:
                    j+=1
            i+=1
        res.append(len(group)+1)
        return max(res)
n=int(input())
tree=[]
for i in range(n-1):
    tree.append(list(map(int,input().split())))
res=[]
for i in range(1,n+1):
    tc=tree.copy()
    j=0
    while j<len(tc):
        if i in tc[j]:
            tc.pop(j)
        else:
            j+=1
    res.append(findMax(tc))
rs=[]
for i in range(n):
    if res[i]==min(res):
        rs.append(i+1)
print(" ".join(str(s) for s in rs),end=" ")