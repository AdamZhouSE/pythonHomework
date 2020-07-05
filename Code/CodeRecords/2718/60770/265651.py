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
    solve()