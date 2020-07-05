res=[]
def dfs(fa,lch,rch,level,p):
    global res
    if len(res)<level:
        res.append([fa[p]])
    else:
        res[level-1].append(fa[p])
    if lch[p]==0 and rch[p]==0:
        return
    if lch[p]!=0:
        dfs(fa,lch,rch,level+1,fa.index(lch[p]))
    if rch[p]!=0:
        dfs(fa,lch,rch,level+1,fa.index(rch[p]))
    return
nr=input().split(' ')
n=int(nr[0])
root=int(nr[1])
fa,lch,rch=[],[],[]
for i in range(n):
    s=input().split(' ')
    fa.append(int(s[0]))
    lch.append(int(s[1]))
    rch.append(int(s[2]))
p=fa.index(root)
dfs(fa,lch,rch,1,p)
for i in range(len(res)):
    res[i]=[str(x) for x in res[i]]
    print('Level '+str(i+1)+' : '+' '.join(res[i]))
for i in range(len(res)):
    res[i]=[int(x) for x in res[i]]
    if i%2!=0:
        res[i].reverse()
        res[i]=[str(x) for x in res[i]]
        print('Level ' + str(i + 1) + ' from right to left: ' + ' '.join(res[i]))
    else:
        res[i]=[str(x) for x in res[i]]
        print('Level ' + str(i + 1) + ' from left to right: ' + ' '.join(res[i]))