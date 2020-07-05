def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
def larger(lists):
    a=lists.copy()
    a.sort()
    if a==lists:
        return True
    else:
        return False
n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n+1)):
    lists.append(0)
lists[0]=root
xs=[]
for i in range(n):
    x=input().split(" ")
    xs.append(x)
    for j in range(len(lists)):
        if(lists[j]==int(x[0])):
            lists[2*j+1]=int(x[1])
            lists[2*j+2]=int(x[2])
targets=[]
for i in range(1,n+1):
    target=[]
    roots=[]
    roots.append(i)
    target.append(i)
    while(roots.count(0)!=len(roots)):
        a=[]
        for j in roots:
            if(j==0):
                a.append(0)
                a.append(0)
                target.append(0)
                target.append(0)
            else:
                a.append(lists[lists.index(j)*2+1])
                a.append(lists[lists.index(j)*2+2])
                target.append(lists[lists.index(j)*2+1])
                target.append(lists[lists.index(j)*2+2])
        roots=a
    res=[]
    out(target,0,len(target),res)
    while(0 in res):
        res.pop(res.index(0))
    targets.append(res)
ans=[]
for i in targets:
    if(larger(i)):
        ans.append(len(i))
if(max(ans)==9):
    print(targets)
print(max(ans))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    