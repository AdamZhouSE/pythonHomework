def solve():
    src=list(input())
    disjointset=[-1 for i in range(len(src))]

    def rootOf(index):
        nonlocal disjointset
        if disjointset[index]==-1:
            return index
        return rootOf(disjointset[index])

    def join(a,b):
        nonlocal disjointset
        roota=rootOf(a)
        rootb=rootOf(b)
        if roota==rootb:
            return
        disjointset[rootb]=roota

    pairs=list(map(lambda x:list(map(int,x.strip('[').strip(']').split(','))),(input()[1:-1].split('],['))))
    for pair in pairs:
        join(pair[0],pair[1])

    groups=[]
    g_index_root={}
    counter=0
    for i in range(len(disjointset)):
        root=rootOf(i)
        index=g_index_root.get(root)
        if index==None:
            g_index_root[root]=counter
            groups.append([i])
            counter+=1
        else:
            groups[index].append(i)

    for group in groups:
        s=list(map(lambda x:src[x],group))
        s.sort()
        for i in range(len(group)):
            src[group[i]]=s[i]

    print(''.join(src))

if __name__ == '__main__':
    solve()def solve():
    k,n=map(int,input().split(','))
    res=[]
    def dfs(k,n,path=[]):
        nonlocal res
        if k==1:
            if n>9 or n<=path[len(path)-1]:
                return
            res.append(path+[n])
        else:
            if len(path)==0:
                low=1
            else:
                low=path[len(path)-1]+1
            up=min(n,9)
            for i in range(low,up+1):
                dfs(k-1,n-i,path+[i])
    dfs(k,n,[])
    print(res)

if  __name__ == '__main__' :
    solve()